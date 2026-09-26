import json

from flask import Flask, render_template, request

from database import Complaint, db
from services.ai_service import analyze_complaint
from services.embedding_service import get_embedding
from services.similarity_service import find_similar_complaints
from services.cluster_service import build_clusters
from services.emerging_issue_service import detect_emerging_issues


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///grievances.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def home():
    return render_template("citizen.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    complaint_text = request.form.get("complaint", "").strip()
    district = request.form.get("district", "").strip()
    ward = request.form.get("ward", "").strip()

    if not complaint_text:
        return "Complaint is required.", 400

    try:
        # 1. Analyze complaint with Gemini
        analysis = analyze_complaint(complaint_text)

        # 2. Prefer citizen-entered location
        if ward:
            analysis["location"] = ward
        elif district and analysis.get("location") == "Not specified":
            analysis["location"] = district

        # 3. Generate semantic embedding
        embedding = get_embedding(complaint_text)

        # 4. Save complaint and AI analysis
        complaint = Complaint(
            complaint_text=complaint_text,
            district=district,
            ward=ward,
            issue=analysis.get("issue"),
            category=analysis.get("category"),
            department=analysis.get("department"),
            location=analysis.get("location"),
            duration=analysis.get("duration"),
            summary=analysis.get("summary"),
            embedding=json.dumps(embedding),
            status="Submitted",
        )

        db.session.add(complaint)
        db.session.commit()

        # 5. Show AI result
        return render_template(
            "analysis.html",
            analysis=analysis,
            complaint_id=complaint.id,
        )

    except Exception as exc:
        db.session.rollback()

        return f"""
        <h2>Something went wrong</h2>
        <p>Please try again.</p>
        <p>Error: {exc}</p>
        <a href="/">Go back</a>
        """, 500


@app.route("/officer", methods=["GET"])
def officer_dashboard():

    try:
        complaints = (
            Complaint.query
            .order_by(Complaint.created_at.desc())
            .all()
        )

        clusters = build_clusters(
            min_similarity=0.90
        )

        emerging_issues = detect_emerging_issues(
            complaints=complaints,
            recent_days=3,
            baseline_days=3,
            min_recent_count=3,
            min_increase_ratio=2.0,
        )

        recent_complaints = complaints[:8]

        return render_template(
            "officer_dashboard.html",
            total_complaints=len(complaints),
            cluster_count=len(clusters),
            emerging_count=len(emerging_issues),
            emerging_issues=emerging_issues,
            clusters=clusters,
            recent_complaints=recent_complaints,
        )

    except Exception as exc:
        return f"""
        <h2>Officer dashboard could not be loaded</h2>
        <p>Please try again.</p>
        <p>Error: {exc}</p>
        <a href="/">Go back</a>
        """, 500


@app.route(
    "/officer/complaint/<int:complaint_id>",
    methods=["GET"]
)
def officer_complaint(complaint_id):

    complaint = db.session.get(
        Complaint,
        complaint_id
    )

    if complaint is None:
        return "Complaint not found.", 404

    try:
        similar_complaints = find_similar_complaints(
            complaint_id=complaint_id,
            top_k=5,
            min_similarity=0.75,
        )

        return render_template(
            "officer.html",
            complaint=complaint,
            similar_complaints=similar_complaints,
        )

    except Exception as exc:
        return f"""
        <h2>Officer intelligence could not be loaded</h2>
        <p>Please try again.</p>
        <p>Error: {exc}</p>
        <a href="/officer">Back to Officer Dashboard</a>
        """, 500


if __name__ == "__main__":
    app.run(debug=True)
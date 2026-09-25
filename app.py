from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("citizen.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    complaint = request.form.get("complaint", "").strip()
    district = request.form.get("district", "").strip()
    ward = request.form.get("ward", "").strip()

    # Temporary analysis data.
    # Real AI analysis will replace this later.
    analysis = {
        "issue": "Water supply interruption",
        "category": "Water Supply",
        "location": ward or district or "Not specified",
        "duration": "5 days",
        "department": "Water / Urban Local Body",
        "summary": (
            "The citizen reports that water supply has not been "
            "available in the reported area for approximately five days."
        ),
    }

    return render_template(
        "analysis.html",
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)
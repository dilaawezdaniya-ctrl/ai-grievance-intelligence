# MVP Scope

## 1. Purpose

This document defines the minimum viable product (MVP) for the
AI Grievance Intelligence & Officer Copilot hackathon prototype.

The goal is to demonstrate one complete, working workflow rather than
a large number of incomplete features.

---

## 2. MVP Goal

Demonstrate that AI can help transform a citizen grievance into
structured and reviewable information, connect it with potentially
related grievances, surface possible emerging patterns, and provide
an officer with an AI-assisted view while keeping final decisions
under human control.

---

## 3. Core MVP Workflow

Citizen
↓
Submit Complaint
↓
AI Complaint Understanding
↓
Structured Complaint
↓
Similar Complaint Detection
↓
Complaint Clustering
↓
Emerging Issue Signal
↓
Officer AI Copilot
↓
Human Review
↓
Status / Action Update
↓
Citizen View

---

## 4. Must-Have Features

### M1 — Citizen Complaint Submission

The citizen can:

* Enter a complaint in natural language.
* Provide basic location information.
* Submit the complaint.
* Receive a complaint ID.

---

### M2 — AI Complaint Understanding

The system should analyze the submitted complaint and extract
structured information such as:

* Main issue
* Category
* Suggested department
* Location
* Duration
* Important entities

The result should be displayed clearly to the user.

---

### M3 — AI Understanding Confirmation

Before final submission, the system should show:

> "We understood your complaint as..."

The citizen should be able to review the extracted information.

---

### M4 — Similar Complaint Detection

The system should compare a complaint against the available
prototype dataset and identify potentially similar complaints.

The result should show:

* Number of similar complaints
* Similarity score or relevance indicator
* Selected related complaints

This will be evaluated on the synthetic/demo dataset.

---

### M5 — Complaint Clustering

The system should group potentially related complaints into clusters.

Example:

* Water Supply
* Road Damage
* Waste Collection
* Electricity

Clusters should be accessible from the officer dashboard.

---

### M6 — Emerging Issue Signal

The system should identify unusual increases in complaint activity
within the prototype dataset.

Example:

> Potential emerging issue detected

The signal must be presented as an indicator for human investigation,
not as a confirmed government finding.

---

### M7 — Officer AI Copilot

The officer should be able to view:

* Complaint summary
* Extracted information
* Similar complaints
* Cluster information
* Relevant workflow information
* AI recommendations

The officer can review and accept or reject AI recommendations.

---

### M8 — Citizen Status View

The citizen should be able to see a simple workflow status such as:

* Submitted
* Under review
* Assigned
* Action taken
* Resolved

Status explanations must be based on recorded application data.

---

## 5. Should-Have Features

These may be added only if the core MVP is working:

* Hindi/English language support
* Voice-to-text input
* Improved dashboard filtering
* Complaint trend charts
* Image attachment
* Better mobile responsiveness

These features must not delay the core workflow.

---

## 6. Future Features

The following are outside the September 30 MVP:

* Production government API integration
* Direct CM Helpline integration
* Native Android/iOS application
* Advanced computer vision
* Large-scale predictive models
* Predictive resolution-time modelling
* Full RAG knowledge system
* Multi-department production deployment
* Advanced authentication and government identity integration
* Large-scale analytics infrastructure

---

## 7. Explicit Non-Goals

The MVP will not attempt to:

* Replace CM Helpline.
* Replace government officers.
* Automatically make final government decisions.
* Claim real-world government performance improvements without
  measured evidence.
* Use confidential government data.
* Present synthetic/demo data as actual MP statistics.

---

## 8. Demo Data Strategy

Because authorized production grievance data is not available to the
prototype team, the MVP will use clearly labelled synthetic/demo data.

The dataset should contain realistic complaint variations across
different categories, locations and languages.

Example categories:

* Water supply
* Road damage
* Waste collection
* Electricity
* Public facilities

The dataset should include both similar and unrelated complaints so
that similarity detection and clustering can be demonstrated.

---

## 9. AI Scope

The MVP AI layer will focus on:

1. Natural-language understanding
2. Structured information extraction
3. Classification assistance
4. Semantic similarity
5. Complaint clustering
6. Emerging-pattern detection
7. Summarization

AI outputs must remain reviewable by humans.

---

## 10. MVP Success Criteria

The MVP is considered functionally complete when a user can:

1. Submit a complaint.
2. Receive structured AI analysis.
3. Confirm the interpretation.
4. Store the complaint.
5. Find related complaints.
6. View the relevant cluster.
7. See a potential emerging issue signal when the test data supports it.
8. Open the officer copilot.
9. Review the AI-generated information.
10. Accept or reject an AI recommendation.
11. Update complaint status.
12. View the updated status from the citizen side.

---

## 11. Scope Prioritization

### P0 — Must work

* Complaint submission
* AI understanding
* Structured extraction
* Similarity
* Clustering
* Officer dashboard
* AI copilot
* Status update

### P1 — Add only after P0 works

* Hindi/English improvements
* Trend charts
* Voice input
* Image attachment
* Advanced filtering

### P2 — Future

* Government integrations
* Advanced AI models
* Mobile application
* Production-scale deployment
* Advanced predictive analytics

---

## 12. Deadline Rule

The team will prioritize:

**Working end-to-end MVP > additional features**

A feature that is incomplete, unreliable or difficult to demonstrate
will not be added simply to increase the feature count.

---

## 13. Current Status

**Status:** MVP scope frozen

**Target:** Working hackathon prototype by September 30, 2026

**Primary demonstration:** Citizen complaint → AI understanding →
similarity/cluster → emerging issue signal → Officer Copilot →
human decision

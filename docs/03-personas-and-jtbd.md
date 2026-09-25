# Personas and Jobs-to-be-Done

## 1. Purpose

This document defines the initial users of the AI Grievance Intelligence
& Officer Copilot product.

These personas are currently product hypotheses based on the documented
grievance workflow and available system information.

They are not a substitute for direct interviews or field research.

The purpose is to create a starting point for:

* Product requirements
* User flows
* Feature prioritization
* UX design
* AI interaction design
* Future user validation

---

# 2. Primary Users

The initial product considers three key users:

1. Citizen
2. Handling / L1 Officer
3. Senior / Monitoring Officer

---

# 3. Persona 1 — Citizen

## Persona Summary

**Role:** Citizen reporting a public-service grievance

**Primary Goal:** Get the problem understood, handled and communicated
clearly without unnecessary effort.

**Primary Interaction:** Submit a complaint, monitor its progress and
understand the current status.

## Goals

* Report a public-service problem.
* Describe the issue in a way that the system can understand.
* Provide relevant location or supporting information.
* Understand what happened after submission.
* Know the current complaint status.
* Understand important status changes.
* Provide feedback on the resolution.

## Potential Frictions

These are initial hypotheses that require validation:

* Difficulty expressing a problem using structured categories.
* Uncertainty about which information is important to provide.
* Difficulty understanding government terminology.
* Uncertainty about what a status actually means.
* Difficulty understanding why a complaint has been escalated or
  remains under review.

These should not be treated as established widespread problems until
validated with users or representative evidence.

## Needs

* Simple complaint description.
* Clear confirmation of what the system understood.
* Guidance when important information is missing.
* Transparent status information.
* Human-readable explanations of workflow events.
* Ability to provide feedback.

---

# 4. Citizen Jobs-to-be-Done

### JTBD-C01 — Report a Problem

> When I experience a public-service problem, I want to describe it in
> simple language so that I can report the issue without needing to
> understand complex administrative categories.

### JTBD-C02 — Confirm Understanding

> When I submit a complaint, I want to see what the system understood
> from my description so that I can correct important misunderstandings
> before continuing.

### JTBD-C03 — Track Progress

> When my complaint is being processed, I want to understand its current
> status so that I know what is happening.

### JTBD-C04 — Understand Escalation

> When my complaint is escalated or reviewed again, I want to understand
> the recorded reason and current stage so that the process is
> transparent to me.

### JTBD-C05 — Provide Feedback

> After my complaint is handled, I want to provide feedback so that my
> experience is reflected in the grievance workflow.

---

# 5. Persona 2 — Handling / L1 Officer

## Persona Summary

**Role:** Officer responsible for reviewing and acting on assigned
grievances.

**Primary Goal:** Understand the complaint and relevant context so that
appropriate action can be taken and documented.

## Goals

* Understand the complaint quickly.
* Review important facts.
* Access relevant complaint information.
* Identify related complaints when useful.
* Review previous workflow activity.
* Record actions or resolution information.
* Respond to escalations or follow-up requirements.
* Support satisfactory resolution.

## Potential Frictions

These are product hypotheses and require validation:

* Time spent interpreting unstructured complaint descriptions.
* Time spent locating related complaints.
* Difficulty seeing patterns across individual complaints.
* Need to review information from different stages of the workflow.
* Need to prepare clear action or resolution information.

## Needs

* Concise complaint summary.
* Extracted key information.
* Related complaint discovery.
* Complaint cluster context.
* Evidence and attachments in one place.
* Workflow history.
* AI assistance that can be verified before action.

---

# 6. Handling Officer Jobs-to-be-Done

### JTBD-O01 — Understand the Complaint

> When I receive a grievance, I want to quickly understand the issue,
> location, relevant details and context so that I can begin appropriate
> action.

### JTBD-O02 — Find Related Complaints

> When a complaint may be related to other cases, I want to discover
> similar complaints so that I can understand whether there is a broader
> pattern.

### JTBD-O03 — Review Context

> When investigating a complaint, I want to see relevant history and
> evidence in one place so that I can make an informed decision.

### JTBD-O04 — Document Action

> When I take action on a complaint, I want to record the important
> information clearly so that the workflow contains an understandable
> action or resolution record.

### JTBD-O05 — Use AI Safely

> When AI provides a recommendation, I want to review the underlying
> information before acting so that I remain responsible for the final
> decision.

---

# 7. Persona 3 — Senior / Monitoring Officer

## Persona Summary

**Role:** Officer or administrator responsible for monitoring grievance
patterns, escalations and broader service-level issues.

**Primary Goal:** Understand what is happening across complaints,
locations or categories and identify cases that may require attention.

## Goals

* Monitor grievance activity.
* Understand clusters of related complaints.
* Identify unusual changes in complaint patterns.
* Review escalated cases.
* Examine repeated or related issues.
* Monitor workflow outcomes.
* Support higher-level review and intervention when necessary.

## Potential Frictions

These are initial hypotheses requiring validation:

* Large numbers of individual complaints may make pattern recognition
  difficult.
* Related cases may need to be reviewed together.
* Emerging trends may require manual monitoring.
* Senior review may require information from multiple complaints.

## Needs

* Aggregated grievance intelligence.
* Complaint clusters.
* Trend information.
* Escalation visibility.
* Drill-down from summary to underlying complaints.
* Evidence-backed AI signals.
* Clear distinction between AI signals and confirmed facts.

---

# 8. Senior / Monitoring Officer Jobs-to-be-Done

### JTBD-S01 — Monitor Patterns

> When monitoring grievance activity, I want to see important patterns
> across locations, categories and time so that I can identify areas
> requiring attention.

### JTBD-S02 — Investigate Clusters

> When a group of similar complaints appears, I want to inspect the
> underlying complaints and evidence so that I can determine whether
> they represent a broader issue.

### JTBD-S03 — Monitor Escalations

> When complaints are escalated, I want to understand the history and
> current state so that I can review the case effectively.

### JTBD-S04 — Review AI Signals

> When the system flags an emerging pattern, I want to inspect the
> underlying evidence so that I can decide whether further action is
> appropriate.

---

# 9. User Relationship

The three users are connected through the same workflow:

Citizen
↓
Complaint
↓
AI Understanding
↓
Handling Officer
↓
Action / Resolution
↓
Citizen Feedback
↓
Senior / Monitoring Review when required

The AI layer supports different users at different stages.

---

# 10. User-to-Feature Mapping

| User             | Need                             | Potential Product Capability     |
| ---------------- | -------------------------------- | -------------------------------- |
| Citizen          | Describe complaint naturally     | AI Complaint Understanding       |
| Citizen          | Correct misunderstandings        | AI Understanding Confirmation    |
| Citizen          | Know current status              | Citizen Status View              |
| Citizen          | Understand escalation            | Citizen-friendly Explanation     |
| Handling Officer | Understand complaint             | AI Summary                       |
| Handling Officer | Find related cases               | Similar Complaint Detection      |
| Handling Officer | Understand broader context       | Complaint Clustering             |
| Handling Officer | Review information before action | Evidence + Workflow Context      |
| Senior Officer   | Monitor patterns                 | Grievance Intelligence Dashboard |
| Senior Officer   | Identify unusual changes         | Emerging Issue Detection         |
| Senior Officer   | Investigate flagged patterns     | Cluster Drill-down               |
| Officer          | Maintain human control           | Human Review / Accept-Reject     |

---

# 11. Product Hypotheses to Validate

The following assumptions should be tested through future interviews,
usability testing, workflow observation or representative data.

### H1

Citizens may benefit from being able to describe complaints naturally
rather than relying entirely on predefined terminology.

### H2

Handling officers may benefit from AI-generated summaries when
complaints contain large amounts of unstructured information.

### H3

Officers may benefit from semantic similarity and clustering when
multiple complaints relate to the same issue.

### H4

Senior or monitoring officers may benefit from visualizing grievance
patterns across locations, categories and time.

### H5

AI-generated explanations may improve citizen understanding of
workflow status when they are grounded in verified system information.

---

# 12. Validation Plan

Before claiming that these are real user pain points, the product team
should validate them through:

1. Interviews with citizens.
2. Interviews with officers where access is available.
3. Usability testing of prototype workflows.
4. Analysis of representative complaint data where legally and
   appropriately available.
5. Task-based experiments comparing manual and AI-assisted workflows.

---

# 13. Key Product Insight

The product serves two connected needs:

### Citizen

**"Understand my problem and tell me what is happening."**

### Officer

**"Understand the problem and help me act on it."**

### Senior / Monitoring Officer

**"Help me understand patterns across many problems."**

Therefore, the product should connect:

**Citizen understanding → Grievance intelligence → Officer action →
Monitoring → Citizen feedback**

---

# 14. Current Status

**Status:** Initial personas and JTBD hypotheses

**Validation:** Required

**Next step:** Validate user needs and convert the strongest validated
needs into the Product Problem Statement and MVP requirements.

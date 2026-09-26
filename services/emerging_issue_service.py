from collections import defaultdict
from datetime import datetime, timedelta, timezone


def _as_utc(value: datetime) -> datetime:
    """Make a datetime timezone-aware in UTC."""
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value.astimezone(timezone.utc)


def detect_emerging_issues(
    complaints,
    recent_days: int = 3,
    baseline_days: int = 3,
    min_recent_count: int = 3,
    min_increase_ratio: float = 2.0,
    now: datetime | None = None,
) -> list[dict]:
    """
    Detect potential emerging issue patterns by comparing complaint
    volume in a recent period with the immediately preceding period.

    This is an explainable MVP signal, not a validated predictive model.
    """

    if now is None:
        now = datetime.now(timezone.utc)
    else:
        now = _as_utc(now)

    recent_start = now - timedelta(days=recent_days)
    baseline_start = recent_start - timedelta(days=baseline_days)

    recent_groups = defaultdict(int)
    baseline_groups = defaultdict(int)

    for complaint in complaints:

        if complaint.created_at is None:
            continue

        created_at = _as_utc(complaint.created_at)

        category = complaint.category or "Uncategorized"
        location = complaint.location or "Not specified"

        group_key = (category, location)

        if recent_start <= created_at <= now:
            recent_groups[group_key] += 1

        elif baseline_start <= created_at < recent_start:
            baseline_groups[group_key] += 1

    signals = []

    all_groups = set(recent_groups) | set(baseline_groups)

    for category, location in all_groups:

        recent_count = recent_groups.get(
            (category, location),
            0,
        )

        baseline_count = baseline_groups.get(
            (category, location),
            0,
        )

        if recent_count < min_recent_count:
            continue

        if baseline_count == 0:
            increase_ratio = None
            is_emerging = True
            increase_percent = None
        else:
            increase_ratio = recent_count / baseline_count
            is_emerging = (
                increase_ratio >= min_increase_ratio
            )
            increase_percent = round(
                (increase_ratio - 1) * 100,
                1,
            )

        if not is_emerging:
            continue

        signals.append(
            {
                "category": category,
                "location": location,
                "recent_count": recent_count,
                "previous_count": baseline_count,
                "increase_ratio": increase_ratio,
                "increase_percent": increase_percent,
                "status": "Potential emerging pattern",
            }
        )

    signals.sort(
        key=lambda item: item["recent_count"],
        reverse=True,
    )

    return signals
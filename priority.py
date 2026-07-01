def get_priority(issue):
    issue_lower = issue.lower()

    high_priority_keywords = [
        "firmware",
        "bbu",
        "power",
        "does not start",
        "not start",
        "stopped",
        "system down",
        "cannot use"
    ]

    normal_priority_keywords = [
        "disk",
        "raid",
        "degraded"
    ]

    low_priority_keywords = [
        "minor",
        "alignment",
        "slightly reduced",
        "monitor",
        "working"
    ]

    for keyword in high_priority_keywords:
        if keyword in issue_lower:
            return "HIGH"
        
    for keyword in normal_priority_keywords:
        if keyword in issue_lower:
            return "NORMAL"
        
    for keyword in low_priority_keywords:
        if keyword in issue_lower:
            return "LOW"
        
    return "CHECK REQUIRED"
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

    for keyword in high_priority_keywords:
        if keyword in issue_lower:
            return "HIGH"
        
    for keyword in normal_priority_keywords:
        if keyword in issue_lower:
            return "NORMAL"
        
    return "CHECK REQUIRED"
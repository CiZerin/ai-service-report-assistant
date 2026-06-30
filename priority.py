def get_priority(issue):
    issue_lower = issue.lower()

    if "firmware" in issue_lower or "bbu" in issue_lower or "power" in issue_lower:
        return "HIGH"
    elif "disk" in issue_lower:
        return "NORMAL"
    else:
        return "CHECK REQUIRED"
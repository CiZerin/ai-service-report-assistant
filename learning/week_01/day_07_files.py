def get_priority(issue):
    issue_lower = issue.lower()

    if "firmware" in issue_lower or "bbu" in issue_lower or "power" in issue_lower:
        return "HIGH"
    elif "disk" in issue_lower:
        return "NORMAL"
    else:
        return "CHECK REQUIRED"

def create_report(service_case):
    report = f"""
=== Service report ===
Engineer: {service_case["engineer"]}
Device: {service_case["device"]}
Serial: {service_case["serial"]}
Issue: {service_case["issue"]}
Status: {service_case["status"]}
Priority: {service_case["priority"]}
Action taken: {service_case["action_taken"]}
Next step: {service_case["next_step"]}
======================
"""
    return report

service_case = {
    "engineer": "Artem",
    "device": "IBM DS3500",
    "serial": "78N6734",
    "issue": "Disk failed",
    "status": "Check FRU part list",
    "action_taken": "Checked disk status and verified error logs",
    "next_step": "Replace failed disk"
}

service_case["priority"] = get_priority(service_case["issue"])
report = create_report(service_case)


with open("service_report.txt", "w") as file:
    file.write(report)

print("Report saved to service_report.txt")
service_cases = [
    {
        "engineer": "Artem",
        "device": "IBM x3500",
        "serial": "78N6234",
        "issue": "Power supply failed",
        "status": "Order new PSU",
        "action_taken": "Checked PSU status and event logs",
        "next_step": "Replace failed PSU"
    },
    {
        "engineer": "Artem",
        "device": "IBM DS3500",
        "serial": "78N6734",
        "issue": "Disk failed",
        "status": "Check FRU part list",
        "action_taken": "Checked disk status and verified error logs",
        "next_step": "Replace failed disk"
    },
    {
        "engineer": "Artem",
        "device": "IBM Storwize v7000",
        "serial": "78N6746",
        "issue": "Unknown warning message",
        "status": "Collect logs",
        "action_taken": "Checked event logs",
        "next_step": "Escalate for analysis"
    },
    {
        "engineer": "Artem",
        "device": "IBM Storwize v3500",
        "serial": "78N6123",
        "issue": "BBU failed",
        "status": "Collect battery logs",
        "action_taken": "Checked battery status and event logs",
        "next_step": "Replace failed BBU"
    }
]

print("=== Service cases ===")

high_count = 0
normal_count = 0
check_required_count = 0

for service_case in service_cases:

    issue_lower = service_case["issue"].lower()

    if "firmware" in issue_lower or "bbu" in issue_lower or "power" in issue_lower:
        service_case["priority"] = "HIGH"
        high_count += 1
    elif "disk" in issue_lower:
        service_case["priority"] = "NORMAL"
        normal_count += 1
    else:
        service_case["priority"] = "CHECK REQUIRED"
        check_required_count += 1

    service_case["summary"] = f'{service_case["device"]} has issue: {service_case["issue"]}. Priority is {service_case["priority"]}.'
    report = f"""
=== Service case ===
Summary: {service_case['summary']}
Engineer: {service_case["engineer"]}
Device: {service_case["device"]}
Serial: {service_case["serial"]}
Issue: {service_case["issue"]}
Status: {service_case["status"]}
Priority: {service_case["priority"]}
Action taken: {service_case["action_taken"]}
Next step: {service_case["next_step"]}
====================
"""

    print(report)

print("=== Summary ===")
print("Total cases:", len(service_cases))
print("High priority cases:", high_count)
print("Normal cases:", normal_count)
print("Check required cases:", check_required_count)
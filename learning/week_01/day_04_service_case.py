service_case = {
    "engineer": "Artem",
    "device": "IBM Storwize v3500",
    "serial": "78N6123",
    "issue": "Power supply failed",
    "status": "Order new PSU",
    "action_taken": "Checked PSU status and event logs",
    "next_step": "Replace failed PSU"
}

issue_lower = service_case["issue"].lower()

if "firmware" in issue_lower or "bbu" in issue_lower or "power" in issue_lower:
    service_case["priority"] = "HIGH"
elif "disk" in issue_lower:
    service_case["priority"] = "NORMAL"
else:
    service_case["priority"] = "CHECK REQUIRED"

service_case["summary"] = f'{service_case["device"]} has issue: {service_case["issue"]}. Priority is {service_case["priority"]}.'

report = f"""
=== Service case ===
Summary: {service_case["summary"]}
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
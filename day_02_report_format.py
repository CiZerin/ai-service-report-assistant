engineer_name = "Artem"
device_name = "IBM x3500"
serial_number = "78N6234"
issue = "   Server doesn't start up   "
status = "   Check lightpass panel   "

issue = issue.strip()
status = status.strip()

issue_lower = issue.lower()

action_taken = "Checked server status and verified error logs"
next_step = "Perform cold restart"

if "firmware" in issue_lower or "bbu" in issue_lower or "power" in issue_lower:
    priority = "HIGH"
elif "disk" in issue_lower:
    priority = "NORMAL"
else:
    priority = "CHECK REQUIRED"

summary = f"{device_name} has issue: {issue}. Priority is {priority}."
report = f"""
=== Service report draft ===
Summary: {summary}
Engineer: {engineer_name}
Device: {device_name}
Serial number: {serial_number}
Issue: {issue}
Status: {status}
Priority: {priority}
Action taken: {action_taken}
Next step: {next_step}
============================
"""

print(report)
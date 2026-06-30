engineer_name = "Artem"
device_name = "IBM DS3500"
serial_number = "78N6734"
issue = "Disk failed"
status = "Inspection required"
is_critical = False
action_taken = "Checked disk status and verified error logs"
next_step = "Replace failed disk and rebuild array"

if is_critical:
    priority = "HIGH"
else:
    priority = "NORMAL"

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
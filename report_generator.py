def create_report(service_case):
    report = f"""
=== SERVICE REPORT ===
Engineer: {service_case["engineer"]}
Device: {service_case["device"]}
Serial: {service_case["serial"]}
Issue: {service_case["issue"]}
Status: {service_case["status"]}
Priority: {service_case["priority"]}
Action taken: {service_case["action_taken"]}
Next step: {service_case["next_step"]}
"""
    return report
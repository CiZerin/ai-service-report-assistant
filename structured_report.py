def create_structured_report(service_case):
    structured_report = {
        "engineer": service_case["engineer"],
        "device": service_case["device"],
        "serial": service_case["serial"],
        "problem": service_case["issue"],
        "status": service_case["status"],
        "priority": service_case["priority"],
        "actions_taken": [service_case["action_taken"]],
        "recommended_next_steps": [service_case["next_step"]],
        "customer_summary": f"{service_case['device']} has issue: {service_case['issue']}. Current priority: {service_case['priority']}."
    }

    return structured_report
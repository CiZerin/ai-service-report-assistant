def create_structured_report(service_case):
    structured_report = {
        "engineer": service_case["engineer"],
        "device": service_case["device"],
        "serial": service_case["serial"],
        "problem": service_case["issue"],
        "status": service_case["status"],
        "priority": service_case["priority"],
        "action_taken": service_case["action_taken"],
        "next_step": service_case["next_step"]
    }

    return structured_report
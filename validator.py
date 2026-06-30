def has_empty_required_fields(service_case):
    required_fields = [
        "engineer",
        "device",
        "serial",
        "issue",
        "status",
        "action_taken",
        "next_step"
    ]

    for field in required_fields:
        if service_case[field] == "":
            return True
    
    return False
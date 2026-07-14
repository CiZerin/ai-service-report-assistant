REQUIRED_FIELDS = [
    "engineer",
    "device",
    "serial",
    "issue",
    "status",
    "action_taken",
    "next_step"
]


def get_missing_required_fields(service_case):
    missing_fields = []

    for field in REQUIRED_FIELDS:
        if service_case.get(field, "") == "":
            missing_fields.append(field)

    return missing_fields


def has_empty_required_fields(service_case):
    return len(get_missing_required_fields(service_case)) > 0
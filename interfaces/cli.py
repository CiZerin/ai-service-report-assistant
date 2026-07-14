def get_service_case_from_user():
    print("=== AI Service Report Assistant ===")
    print("Enter service case details below.")
    print()

    engineer = input("Enter engineer name: ").strip()
    device = input("Enter device model: ").strip()
    serial = input("Enter serial number: ").strip()
    issue = input("Enter issue: ").strip()
    status = input("Enter current status: ").strip()
    action_taken = input("Enter action taken: ").strip()
    next_step = input("Enter next step: ").strip()

    service_case = {
        "engineer": engineer,
        "device": device,
        "serial": serial,
        "issue": issue,
        "status": status,
        "action_taken": action_taken,
        "next_step": next_step
    }

    return service_case


def ask_use_ai():
    answer = input("Use AI-generated report? yes/no: ").strip().lower()

    if answer == "yes" or answer == "y":
        return True

    if answer == "no" or answer == "n":
        return False

    print("Unknown answer. Manual report will be used.")
    return False
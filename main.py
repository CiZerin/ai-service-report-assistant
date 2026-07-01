from datetime import datetime
from priority import get_priority
from report_generator import create_report
from file_writer import save_report, save_json_report
from structured_report import create_structured_report
from validator import has_empty_required_fields

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


def main():
    service_case = get_service_case_from_user()

    if has_empty_required_fields(service_case):
        print("Warning: Some required fields are empty. Report was not created.")
        exit()

    service_case["priority"] = get_priority(service_case["issue"])
    report = create_report(service_case)
    structured_report = create_structured_report(service_case)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    txt_filename = f"reports/service_report_{timestamp}.txt"
    json_filename = f"reports/service_report_{timestamp}.json"

    save_report(txt_filename, report)
    save_json_report(json_filename, structured_report)

    print()
    print("Report created successfully.")
    print(f"Text report saved to: {txt_filename}")
    print(f"JSON report saved to: {json_filename}")


main()
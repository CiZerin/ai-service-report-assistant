from priority import get_priority
from report_generator import create_report
from file_writer import save_report
from structured_report import create_structured_report

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

service_case["priority"] = get_priority(service_case["issue"])
report = create_report(service_case)
structured_report = create_structured_report(service_case)

save_report("reports/service_report.txt", report)

print(structured_report)
print("Report saved to service_report.txt")
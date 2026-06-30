from priority import get_priority
from report_generator import create_report
from file_writer import save_report

engineer = input("Enter engineer name: ")
device = input("Enter device model: ")
serial = input("Enter serial number: ")
issue = input("Enter issue: ")
status = input("Enter current status: ")
action_taken = input("Enter action taken: ")
next_step = input("Enter next step: ")

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

save_report("service_report.txt", report)

print("Report saved to service_report.txt")
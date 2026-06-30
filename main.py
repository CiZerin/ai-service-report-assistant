from priority import get_priority
from report_generator import create_report
from file_writer import save_report

service_case = {
    "engineer": "Artem",
    "device": "IBM DS3500",
    "serial": "78N6734",
    "issue": "Disk failed",
    "status": "Check FRU part list",
    "action_taken": "Checked disk status and verified error logs",
    "next_step": "Replace failed disk"
}

service_case["priority"] = get_priority(service_case["issue"])
report = create_report(service_case)

save_report("service_report.txt", report)

print("Report saved to service_report.txt")
from datetime import datetime
from file_writer import save_report, save_json_report


def save_report_result(result):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    txt_filename = f"reports/service_report_{timestamp}.txt"
    json_filename = f"reports/service_report_{timestamp}.json"

    save_report(txt_filename, result["text_report"])
    save_json_report(json_filename, result["structured_report"])

    return {
        "txt_filename": txt_filename,
        "json_filename": json_filename
    }
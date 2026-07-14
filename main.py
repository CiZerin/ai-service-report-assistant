from interfaces.cli import get_service_case_from_user, ask_use_ai
from report_service import create_service_report
from storage.file_storage import save_report_result


def main():
    service_case = get_service_case_from_user()
    use_ai = ask_use_ai()

    result = create_service_report(service_case, use_ai)

    if not result["success"]:
        print(f"Warning: {result['error']} Report was not created.")
        return

    if result["used_fallback"]:
        print("AI request failed. Manual report will be generated instead.")

    saved_files = save_report_result(result)

    print()
    print("Report created successfully.")
    print(f"Text report saved to: {saved_files['txt_filename']}")
    print(f"JSON report saved to: {saved_files['json_filename']}")


if __name__ == "__main__":
    main()
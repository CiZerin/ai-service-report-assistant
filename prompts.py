def create_service_report_prompt(service_case_notes):
    prompt = f"""
Turn the following rough service notes into a clear service report.

Use this structure:
- Device
- Serial number
- Issue
- Current status
- Action taken
- Recommended next step
- Customer summary

Service notes:
{service_case_notes}
"""
    return prompt
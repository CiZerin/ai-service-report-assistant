from priority import get_priority
from report_generator import create_report
from structured_report import create_structured_report
from validator import has_empty_required_fields
from ai_client import generate_ai_report


def create_service_case_notes(service_case):
    notes = f"""
Engineer: {service_case["engineer"]}
Device: {service_case["device"]}
Serial number: {service_case["serial"]}
Issue: {service_case["issue"]}
Current status: {service_case["status"]}
Action taken: {service_case["action_taken"]}
Next step: {service_case["next_step"]}
Priority: {service_case["priority"]}
"""
    return notes


def create_service_report(service_case, use_ai=False):
    if has_empty_required_fields(service_case):
        return {
            "success": False,
            "error": "Some required fields are empty.",
            "text_report": None,
            "structured_report": None,
            "used_ai": False,
            "used_fallback": False
        }

    service_case["priority"] = get_priority(service_case["issue"])

    used_ai = False
    used_fallback = False

    if use_ai:
        service_case_notes = create_service_case_notes(service_case)
        ai_report = generate_ai_report(service_case_notes)

        if ai_report.startswith("AI report generation failed"):
            text_report = create_report(service_case)
            used_fallback = True
        else:
            text_report = ai_report
            used_ai = True

    else:
        text_report = create_report(service_case)

    structured_report = create_structured_report(service_case)

    return {
        "success": True,
        "error": None,
        "text_report": text_report,
        "structured_report": structured_report,
        "used_ai": used_ai,
        "used_fallback": used_fallback
    }
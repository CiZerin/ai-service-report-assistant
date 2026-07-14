import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from prompts import create_service_report_prompt


def generate_ai_report(service_case_notes):
    load_dotenv()

    api_key = os.getenv("YANDEX_API_KEY")
    model_uri = os.getenv("YANDEX_MODEL_URI")

    if not api_key:
        return "AI report generation failed: YANDEX_API_KEY is missing."

    if not model_uri:
        return "AI report generation failed: YANDEX_MODEL_URI is missing."

    client = OpenAI(
        api_key=api_key,
        base_url="https://ai.api.cloud.yandex.net/v1"
    )

    prompt = create_service_report_prompt(service_case_notes)

    try:
        response = client.chat.completions.create(
            model=model_uri,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except OpenAIError as error:
        return f"AI report generation failed: {error}"

    except Exception as error:
        return f"AI report generation failed: unexpected error: {error}"
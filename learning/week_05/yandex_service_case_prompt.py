import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

api_key = os.getenv("YANDEX_API_KEY")
model_uri = os.getenv("YANDEX_MODEL_URI")

client = OpenAI(
    api_key=api_key,
    base_url="https://ai.api.cloud.yandex.net/v1"
)

service_case = """
Engineer: Artem
Device: MRI cooling unit
Serial: MCU-2241
Issue: Cooling system alarm. Device stopped during operation.
Status: Device not operational.
Action taken: Checked logs, inspected cooling pump, found low coolant level.
Next step: Refill coolant and test system stability.
"""

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
{service_case}
"""

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

    print(response.choices[0].message.content)

except OpenAIError as error:
    print("Yandex AI request failed.")
    print(error)
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

try:
    response = client.chat.completions.create(
        model=model_uri,
        messages=[
            {
                "role": "user",
                "content": "Explain API in one simple sentence for a beginner Python student."
            }
        ]
    )

    print(response.choices[0].message.content)

except OpenAIError as error:
    print("Yandex AI request failed.")
    print(error)
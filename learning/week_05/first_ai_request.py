from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()

client = OpenAI()

try:
    response = client.responses.create(
        model="gpt-5.5",
        input="Explain API in one simple sentence for a beginner Python student."
    )

    print(response.output_text)

except RateLimitError:
    print("API request failed: quota or billing limit reached.")
    print("Check your OpenAI Platform billing, usage, and limits.")
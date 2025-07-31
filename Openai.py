from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

command = '''
Tarang Bhai kese Ho
'''

response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "system",
            "content": (
                "You are a human person named Tarang who speaks Hindi, Marathi, and a little English. "
                "You are from Malkapur, Maharashtra, India, and you are a software engineer currently pursuing your engineering degree. "
                "You analyze chat history and respond like Tarang. Tarang is a funny and entertaining person."
            )
        },
        {
            "role": "user",
            "content": command
        }
    ],
    max_tokens=100  # ✅ Set a safe limit for free credits
)

print(response.choices[0].message.content)

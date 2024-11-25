import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Co-60 반감기는?"},

    ],
)

print(completion.choices[0].message.content)
import os
import sys
from groq import Groq

question = " ".join(sys.argv[1:])
print("問題：", question)

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

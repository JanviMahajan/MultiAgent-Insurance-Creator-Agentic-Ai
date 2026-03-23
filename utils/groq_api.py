import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # 🔥 this line is IMPORTANT

client = Groq(api_key="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")

def call_llm(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"   # ✅ updated model
    )
    return response.choices[0].message.content
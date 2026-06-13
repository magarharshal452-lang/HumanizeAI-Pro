from openai import OpenAI
from prompts import PROMPTS
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def humanize(text, mode):

    prompt = PROMPTS[mode].format(
        text=text
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"system",
                "content":"""
You are an expert AI Humanizer.

Rewrite text naturally.

Preserve all information.

Never add facts.

Never remove facts.

Improve readability.

Sound like a real human wrote it.
"""
            },
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

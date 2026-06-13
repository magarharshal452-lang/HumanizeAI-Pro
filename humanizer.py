from transformers import pipeline
from prompts import PROMPTS

generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base"
)

def humanize(text, mode):

    prompt = PROMPTS[mode].format(text=text)

    result = generator(
        prompt,
        max_length=512,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]

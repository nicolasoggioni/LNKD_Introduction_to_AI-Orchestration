import os

from openai import OpenAI
from IPython.display import display, HTML

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

def get_completion_from_messages(messages, model="gpt-4", temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message.content

prompt = input("Enter your prompt here: ")

responses = get_completion_from_messages(prompt)
print(responses)

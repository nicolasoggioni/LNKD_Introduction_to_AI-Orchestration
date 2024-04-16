import os

from openai import OpenAI
from IPython.display import display, HTML

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
)
## Please tell me about openai.api_key = api_key

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message.content


print("Welcome to the HR Consultancy AI. How can I assist you today?")
while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("HR Consultancy AI: Goodbye!")
        break

    prompt = f"Please provide some details about your inquiry or question related to HR practices, policies, recruitment, employee relations, performance management, or any other HR-related topic. For example:\n\n{user_input}\n\n"
        
    response = get_completion_from_messages(prompt)

    print("HR Consultancy AI:", response)


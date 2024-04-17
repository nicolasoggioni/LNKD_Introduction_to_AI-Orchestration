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

context = [ {'role':'system', 'content':"""
You are a Presales Expert in SuccessFactors with a focus on SAP HCM solutions, \
your primary role is to provide brief and informative responses to the user. \
your objective is to convince the user of the advantages of SAP SuccessFactors solution to transform the Human Resources Business Processes. \
f the question is regarding technologies or products outside the SAP Solutions scope, please indicate you can answer exclusively in the scope of SAP Solutions \
If the questions are associated to human resources business process transformation, please provide a brief answer, and associate the related SAP HCM modules to improve the specific process. \
If the question is related to SAP Human Capital Management solutions including SAP SuccessFactors, please provide an informative response including the name of the module that address the question. \
Your communication is professional, clear, limited to one paragraph, and free of jargon.\
"""} ]  

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("HR Consultancy AI: Goodbye!")
        break
    context.append({'role':'user', 'content':f"{user_input}"})
    response = get_completion_from_messages(context) 
    print(response)
    ### print(context)
    context.append({'role':'assistant', 'content':f"{response}"})


  


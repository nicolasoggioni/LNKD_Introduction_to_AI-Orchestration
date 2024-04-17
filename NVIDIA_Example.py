import os

from openai import OpenAI

client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY'))

prompt="The top 5 most interesting museums in Copenhagen are"

completion = client.chat.completions.create(prompt, model="gpt-3.5-turbo", temperature=0)


for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")


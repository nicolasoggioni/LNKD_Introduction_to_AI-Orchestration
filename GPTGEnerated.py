import openai

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key_here'

def ask_chat_gpt(question):
    try:
        # Define parameters for the completion
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=50
        )
        # Extract and return the generated response
        answer = response['choices'][0]['text'].strip()
        return answer
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Ask for user input
    user_question = input("Ask me a question: ")

    # Call the function to generate a response
    answer = ask_chat_gpt(user_question)

    # Display the response
    if answer:
        print("OpenAI ChatGPT says:", answer)
    else:
        print("Sorry, I couldn't generate a response.")

if __name__ == "__main__":
    main()
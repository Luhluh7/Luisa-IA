from openai import OpenAI


client = OpenAI(api_key=" ")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="got-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if _name_ == "_main_":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["quit", "exit", "bye", "sair", "tchau"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)

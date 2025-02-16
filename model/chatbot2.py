import os
from Groq_Audio import get_clean_text  # Import function to get text from speech
from image_groq import analyze_image   # Import function to analyze an image

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq


def main():
    """Main function to run chatbot."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Groq API key not found. Please set it in the .env file.")

    model = 'llama3-8b-8192'
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)

    system_prompt = 'You are a friendly conversational chatbot'
    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)

    while True:
        print("\nChoose an input method:")
        print("1. Speak Audio")
        print("2. Upload an Image")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            user_question = get_clean_text()  # Get cleaned text from speech
        elif choice == "2":
            image_response = analyze_image("image/image.jpg")  # Analyze the image
            print("\nImage Analysis:", image_response)  # Show the result
            continue  # Skip chatbot processing and ask again
        else:
            print("Invalid choice, please enter 1 or 2.")
            continue

        if not user_question.strip():
            print("No input detected. Try again.")
            continue  # Skip empty input

        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ])

        conversation = LLMChain(llm=groq_chat, prompt=prompt, verbose=False, memory=memory)
        response = conversation.predict(human_input=user_question)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

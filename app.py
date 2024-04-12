import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['GOOGLE_API_KEY'] = "AIzaSyDE5aHljyoe2mS3qIcz0bDeFh6xPZp4jJM"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

chat_model = genai.GenerativeModel('gemini-pro')
chat = chat_model .start_chat(history=[])

response = chat.send_message("Which is one of the best place to visit in India during summer?")
print(response.text)
response = chat.send_message("Tell me more about that place in 50 words")
print(response.text)
print(chat.history)



llm = ChatGoogleGenerativeAI(model="gemini-pro")
batch_responses = llm.batch(
    [
        "Who is the Prime Minister of India?",
        "What is the capital of India?",
    ]
)
for response in batch_responses:
    print(response.content)
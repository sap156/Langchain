from langchain_core.messages import SystemMessage , HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo")

messages = [
    SystemMessage(content="You are an expert in soical media content strategy."),
    HumanMessage(content="Give a short tip to improve my Medium blog post visibility."),
]

result = llm.invoke(messages)
print(result.content)
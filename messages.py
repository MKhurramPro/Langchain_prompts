from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="",
    task="text_generation"
)

model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="Tell about Langchain in 5 lines")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Instruct",
    task="text_generation",
    temperature=1.5
)



model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
    ("system","You are helpful {domain} Expert"),
    ("human","Explain in simple terms,What is {topic}")
])


prompt = chat_template.invoke({"domain":"cricket","topic":"Dusra"})

print(prompt)
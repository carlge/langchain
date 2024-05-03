from langchain_community.llms import Ollama

# using num_predict instead of max_tokens
llm = Ollama(
    model="llama3:8b",
    temperature=0.8,
    num_predict=60,
)
response = llm.invoke("Tell me a joke")
print(response)

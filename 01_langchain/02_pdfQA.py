from flask import Flask, request, render_template
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain.prompts.chat import ChatPromptTemplate

# load from the vector store
PRESIST_DIR = r".\chroma_db"
EMBEDDING = GPT4AllEmbeddings()
vectorstore = Chroma(embedding_function=EMBEDDING, persist_directory=PRESIST_DIR)

# Template creation for make bot with Model.
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

# Create llm model
llm = Ollama(model="llama3:8b", temperature=0)
document_chain = create_stuff_documents_chain(llm, prompt)

# Create retriver and revierval chain
retriever = vectorstore.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# qa_query = "What is MapReduce?"
# response = retrieval_chain.invoke({"input": qa_query})
# print(response["answer"])

# Create a simple UI
app = Flask(__name__)  # Flask APP


# Home
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")
        response = retrieval_chain.invoke({"input": question})
        return render_template("index.html", result=response["answer"])
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

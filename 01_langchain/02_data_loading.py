import os
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

# load the document and split it into chunks
DOC_DIR = r".\docs"  # location to save docs
docs = []
for file in os.listdir(DOC_DIR):
    file_path = os.path.join(DOC_DIR, file)
    print(file_path)
    loader = PyPDFLoader(file_path)
    docs.extend(loader.load())

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=10, separators=["\n", "\n\n"]
)
r_splited_docs = r_splitter.split_documents(docs)

# save in the vector store
PRESIST_DIR = r".\chroma_db"
EMBEDDING = GPT4AllEmbeddings()
vectorstore = Chroma.from_documents(
    documents=r_splited_docs,
    collection_name="docs",
    embedding=EMBEDDING,
    persist_directory=PRESIST_DIR,
)

# query the DB
# query = "What is mapreduce"
# docs = vectorstore.similarity_search(query)
# # print results
# print(docs[0].page_content)

vectorstore.persist()

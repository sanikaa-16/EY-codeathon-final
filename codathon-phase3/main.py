from fastapi import FastAPI, Query
from llama_cpp import Llama
import pypdf
import textwrap
from sentence_transformers import SentenceTransformer
import chromadb

# Initialize FastAPI app
app = FastAPI()

# Load Llama model
llm = Llama(model_path="/path_to_model", n_ctx=2048)

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="pdf_chunks")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    pdf_reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to chunk text
def chunk_text(text, chunk_size=500):
    return textwrap.wrap(text, chunk_size)

# Function to store chunks in ChromaDB
def store_pdf_data(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)

    for idx, chunk in enumerate(chunks):
        embedding = embedding_model.encode(chunk).tolist()
        collection.add(ids=[str(idx)], embeddings=[embedding], metadatas=[{"text": chunk}])

# Load PDF data (Run this once before queries)
store_pdf_data("443_Disaster_04_(2).pdf")

# Function to retrieve relevant chunks
def retrieve_relevant_chunks(query, top_k=3):
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return [res["text"] for res in results["metadatas"][0]]

# FastAPI route to handle queries
@app.get("/query")
def get_answer(query: str = Query(..., description="User query related to PDF data")):
    # Retrieve context from ChromaDB
    retrieved_chunks = retrieve_relevant_chunks(query)
    context = "\n".join(retrieved_chunks)

    # Construct Llama prompt
    prompt = f"Use the following context to answer the query:\n\n{context}\n\nQuery: {query}\nAnswer:"

    # Get response from Llama
    response = llm(prompt, max_tokens=200)

    return {"query": query, "response": response["choices"][0]["text"]}

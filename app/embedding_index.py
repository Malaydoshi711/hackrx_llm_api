import faiss
import numpy as np
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedder = OpenAIEmbeddings()

index = None
stored_chunks = []

def embed_and_search(chunks, query, k=5):
    global index, stored_chunks
    stored_chunks = chunks
    vectors = embedder.embed_documents(chunks)
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors).astype("float32"))

    q_vec = embedder.embed_query(query)
    D, I = index.search(np.array([q_vec]).astype("float32"), k)
    return [stored_chunks[i] for i in I[0]]

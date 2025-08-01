import fitz  # PyMuPDF
import httpx
from langchain.text_splitter import RecursiveCharacterTextSplitter

async def load_and_split_docs(url):
    r = await httpx.AsyncClient().get(url)
    with open("temp.pdf", "wb") as f:
        f.write(r.content)
    doc = fitz.open("temp.pdf")
    text = "\n".join([page.get_text() for page in doc])

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_text(text)

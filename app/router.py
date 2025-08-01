from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import BaseModel
from app.auth import verify_token
from app.document_loader import load_and_split_docs
from app.embedding_index import embed_and_search
from app.llm_reasoner import query_llm

router = APIRouter()

class RunRequest(BaseModel):
    documents: str
    questions: list[str]

@router.post("/run")
async def run(request: Request, body: RunRequest, token: None = Depends(verify_token)):
    try:
        chunks = await load_and_split_docs(body.documents)
        answers = []
        for question in body.questions:
            relevant_chunks = embed_and_search(chunks, question)
            decision = query_llm(question, relevant_chunks)
            answers.append(decision)
        return {"answers": answers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

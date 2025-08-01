from fastapi import FastAPI
from app.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HackRX 6.0 LLM API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/hackrx")

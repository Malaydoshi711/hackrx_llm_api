from fastapi import Header, HTTPException
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_TOKEN = os.getenv("BEARER_TOKEN")

def verify_token(authorization: str = Header(...)):
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or token != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

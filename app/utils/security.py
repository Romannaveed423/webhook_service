from fastapi import Header, HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SHARED_SECRET = os.getenv("SHARED_SECRET")
if not SHARED_SECRET:
    raise ValueError("SHARED_SECRET is not set in the environment variables")

def verify_signature(x_signature: str = Header(...)):
    if x_signature != SHARED_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid signature"
        )

from fastapi import APIRouter
from app.services.generate_service import generate_post

router = APIRouter()

@router.post("/")
def generate_content(topic: str):
    post = generate_post(topic)
    return {"generated_post": post}

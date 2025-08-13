from app.services.openai_service import generate_text
from app.utils.safety import check_content_safety

def generate_post(topic: str) -> str:
    post = generate_text(f"Write a LinkedIn post about {topic}")
    if check_content_safety(post):
        return post
    return "[Content flagged as unsafe]"

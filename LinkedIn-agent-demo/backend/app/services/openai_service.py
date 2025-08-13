import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_text(prompt: str) -> str:
    # Mock response for speed
    return f"[AI Generated Post based on: {prompt}]"

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.post("/")
def schedule_post(content: str, schedule_time: str):
    return {
        "content": content,
        "schedule_time": schedule_time,
        "status": "Scheduled"
    }

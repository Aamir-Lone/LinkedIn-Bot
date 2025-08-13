from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_analytics():
    return {
        "likes": 120,
        "comments": 45,
        "shares": 15
    }

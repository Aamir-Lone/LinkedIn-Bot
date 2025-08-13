from backend.app.services.schedule_service import schedule_post
from datetime import datetime

def test_schedule_post():
    result = schedule_post("Test Post", datetime.now())
    assert "content" in result

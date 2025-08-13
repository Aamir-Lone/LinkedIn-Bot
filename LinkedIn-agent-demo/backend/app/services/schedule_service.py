from datetime import datetime

def schedule_post(content: str, schedule_time: datetime):
    return {"content": content, "schedule_time": schedule_time}

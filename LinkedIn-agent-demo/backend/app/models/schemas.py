from pydantic import BaseModel

class PostRequest(BaseModel):
    topic: str

class ScheduleRequest(BaseModel):
    content: str
    schedule_time: str

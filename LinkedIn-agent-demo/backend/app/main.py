from fastapi import FastAPI
from app.api.v1 import auth, generate, schedule, analytics

app = FastAPI(title="LinkedIn AI Agent", version="1.0")

# Include API routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(generate.router, prefix="/api/v1/generate", tags=["Content Generation"])
app.include_router(schedule.router, prefix="/api/v1/schedule", tags=["Scheduling"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])

@app.get("/")
def home():
    return {"message": "LinkedIn AI Agent API is running 🚀"}

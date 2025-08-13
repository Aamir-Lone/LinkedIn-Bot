# LinkedIn AI Agent

This is a demo project that:
- Generates LinkedIn posts using AI (mocked for speed)
- Schedules posts
- Displays mock analytics

## Run Locally

```bash
# Install backend
cd backend && pip install -r requirements.txt

# Run backend
uvicorn app.main:app --reload

# Install frontend
cd frontend && pip install -r requirements.txt

# Run frontend
streamlit run streamlit_app.py






#!/bin/bash
echo "🚀 Starting Backend..."
uvicorn backend.app.main:app --reload &

echo "🚀 Starting Frontend..."
streamlit run frontend/streamlit_app.py

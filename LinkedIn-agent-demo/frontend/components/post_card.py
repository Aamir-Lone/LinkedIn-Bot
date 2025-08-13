import streamlit as st

def render_post_card(content: str, likes: int = 0, comments: int = 0, shares: int = 0):
    st.markdown(f"""
    <div style="border:1px solid #ccc; padding: 10px; border-radius: 10px;">
        <p>{content}</p>
        <small>👍 {likes} | 💬 {comments} | 🔄 {shares}</small>
    </div>
    """, unsafe_allow_html=True)

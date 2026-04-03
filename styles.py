# styles.py
import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    .stApp { background-color: white; }
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        margin-bottom: 20px;
    }
    .stButton>button { width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)
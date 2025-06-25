

import streamlit as st
import openai

API_KEY = st.secrets["groq_api_key"]
client = openai.OpenAI(api_key=API_KEY, base_url="https://api.groq.com/openai/v1")

def ask_groq(prompt):
    response = client.chat.completions.create(
        model="mistral-saba-24b",
        messages=[
            {"role": "system", "content": "You are an AI assistant helping with technical interview preparation."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

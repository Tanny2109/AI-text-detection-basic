import streamlit as st
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="yuchuantian/AIGC_detector_env2")
# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

with st.form("AI detection"):
    text = st.text_area("Enter text here...")
    btn = st.form_submit_button("enter")

if btn: 
    out = pipe(text)
    label = out[0]['label']
    if label == 0:
        classify='bot generated.'
    else:
        classify='human generated.'
    st.write(classify)
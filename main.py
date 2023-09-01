"""
Install all required packages:
run 'pip install -r requirements.txt'

To Launch Streamlit:
run 'streamlit run con_sum.py' in terminal and you will get local n network urls
"""

import streamlit as st
import newspaper
from txtai.pipeline import Summary
import nltk

nltk.download("punkt")

st.title("Content Summarizer")

choice = st.selectbox("You want summary of:", ["Text", "Article"])

if choice == "Text":
    st.subheader("Text Sumarization:")
    input_text = st.text_area("", placeholder="Enter your text here")
    if input_text is not None:
        if st.button("Summarize Text"):
            tab1, tab2 = st.tabs(["Full Text", "Summary"])
            with tab1:
                st.info(input_text)
            with tab2:
                summary = Summary()
                result = summary(input_text)
                st.success(result)

if choice == "Article":
    st.subheader("Article Sumarization:")

    url = st.text_input("", placeholder="Paste the article link")
    article = newspaper.Article(url)

    article.download()
    article.parse()
    article.nlp()

    img = article.top_image
    st.image(img)

    st.subheader("Title: ", article.title)

    tab1, tab2 = st.tabs(["Full Text", "Summary"])
    with tab1:
        article.text

    with tab2:
        st.write(article.summary)

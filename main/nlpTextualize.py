import streamlit as st
from time import sleep
from stqdm import stqdm
import pandas as pd
from transformers import pipeline
import json
import spacy
import spacy_streamlit

def draw_header():
    st.write(
        """
        ## Key Features:
        - **Advanced Text Summarization**: Generate succinct summaries from extensive text documents.
        - **Text Completion**: Automatically complete sentences or paragraphs seamlessly.
        - **Sentiment Analysis**: Assess and interpret the sentiment conveyed in written content.
        - **Named Entity Recognition (NER)**: Identify and classify entities within the text.
        - **Question Answering**: Provide contextual information and answer specific queries.
        """
    )

# Sidebar
with st.sidebar:
    st.write("# 💫 nlpTextualize")
    st.write("""
        Welcome to **nlpTextualize**! This application harnesses advanced Natural Language Processing (NLP) models to facilitate a variety of sophisticated text processing tasks.
    """)
    
    menu = ["--Select--", "Summarizer", "Named Entity Recognition", "Sentiment Analysis", "Question Answering", "Text Completion"]
    choice = st.selectbox("Select a Feature", menu)

# Main function
def main():
    if choice == "--Select--":
        st.write("""
            This application offers a variety of NLP functionalities to help you analyze and understand textual data effectively.
        """)
        st.image('image.png')
        draw_header()  # Display key features after the intro in the sidebar

    elif choice == "Summarizer":
        st.subheader("Text Summarization")
        raw_text = st.text_area("Input Text", "Enter your text here...")
        num_words = st.number_input("Summary Length (Number of Words)", min_value=1, value=50)

        if raw_text and num_words:
            summarizer = pipeline('summarization')
            summary = summarizer(raw_text, min_length=num_words, max_length=100)
            result_summary = summary[0]['summary_text']
            st.write("### Summary:")
            st.write(result_summary.capitalize())

    elif choice == "Named Entity Recognition":
        nlp = spacy.load("en_core_web_sm")
        st.subheader("Named Entity Recognition")
        raw_text = st.text_area("Input Text for NER", "Enter your text here...")

        if raw_text:
            doc = nlp(raw_text)
            for _ in range(50):
                sleep(0.1)
            spacy_streamlit.visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title="Extracted Named Entities")

    elif choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        sentiment_analysis = pipeline("sentiment-analysis")
        raw_text = st.text_area("Input Text for Sentiment Analysis", "Enter your text here...")

        if raw_text:
            result = sentiment_analysis(raw_text)[0]
            sentiment = result['label']
            for _ in range(50):
                sleep(0.1)
            st.write(f"### Sentiment: {sentiment} 🎉")

    elif choice == "Question Answering":
        st.subheader("Question Answering")
        question_answering = pipeline("question-answering")
        context = st.text_area("Context", "Enter the context here...")
        question = st.text_area("Your Question", "Enter your question here...")

        if context and question:
            result = question_answering(question=question, context=context)
            st.write("### Answer:")
            st.write(result['answer'].capitalize())

    elif choice == "Text Completion":
        st.subheader("Text Completion")
        text_generation = pipeline("text-generation")
        message = st.text_area("Input Incomplete Text", "Enter your incomplete text here...")

        if message:
            generator = text_generation(message, max_length=50)
            generated_text = generator[0]['generated_text']
            st.write("### Completed Text:")
            st.write(generated_text)

if __name__ == '__main__':
    main()

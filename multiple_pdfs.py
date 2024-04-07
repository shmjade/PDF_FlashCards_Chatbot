import streamlit as st #graphical interface
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from flashcards import create_anki_cards, interface_flashcards
import openai
from htmlTemplates import css
from chatbot import interface_chatbot, handle_userinput, get_pdf_text, get_conversation_chain, get_vectorstore, get_text_chunks

def main():

    load_dotenv()

    st.set_page_config(page_title="Chat with multiple pdfs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🤖 Chatbot", "🗃 Flashcards generator"])
    tab1.subheader("🤖 Ask questions about your pdf")

    tab2.subheader("Flashcardssssssss")
    if "text_pdf" not in st.session_state:
        st.session_state.text_pdf = ""

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):  # shows loading icon
                st.session_state.text_pdf = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(st.session_state.text_pdf)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
        with tab1:
            interface_chatbot()
        with tab2:
            flashcards = create_anki_cards(st.session_state.text_pdf)
            interface_flashcards(flashcards)

if __name__ == '__main__':
    main()
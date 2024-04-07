import streamlit as st #graphical interface
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from flashcards import create_anki_cards
import openai
# import chromadb
from htmlTemplates import css
from chatbot import handle_userinput, get_pdf_text, get_conversation_chain, get_vectorstore, get_text_chunks

def main():
    load_dotenv()

    st.set_page_config(page_title="Chat with multiple pdfs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🤖 Chatbot", "🗃 Flashcards generator"])
    tab1.subheader("🤖 Ask questions about your pdf 🤔")

    tab2.subheader("A tab with the data")


    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple pdfs :books:")
    user_question = st.text_input("Ask a question about your documents:", placeholder="Type your question here")

    if user_question:
        handle_userinput(user_question)

    #st.write(user_template.replace("{{MSG}}", "hello robot"), unsafe_allow_html=True)
    #st.write(bot_template.replace("{{MSG}}", "hello human"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):  # shows loading icon
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
                #st.write(text_chunks)
                st.write("Flashcards:")
                st.write(create_anki_cards(raw_text))

if __name__ == '__main__':
    main()
import openai
import streamlit as st

current_index = 0

# dividing text into smaller chunks:
def divide_text(text, section_size):
    sections = []
    start = 0
    end = section_size
    while start < len(text):
        section = text[start:end]
        sections.append(section)
        start = end
        end += section_size
    return sections

def display_flashcards(flashcards):
    st.subheader("Flashcards:")
    for card in flashcards:
        st.write("Question:", card["question"])
        st.write("Answer:", card["answer"])
        st.write("---")

def create_anki_cards(pdf_text):
    SECTION_SIZE = 1000
    divided_sections = divide_text(pdf_text, SECTION_SIZE)
    st.session_state.generated_flashcards = []

    for i, text in enumerate(divided_sections):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Create flashcards about the provided text using a format: question;answer next line question;answer etc. Keep question and the corresponding answer on the same line. Here are some examples:\n\nWhat's the capital of Brazil?;Brasília\n- 2+3?;5. Here is the text: " + text}        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages, 
            temperature=0.3,
            max_tokens=2048
        )
        st.write("lalala: ", response)
        response_from_api = response["choices"][0]["message"]["content"].split("\n")
        st.write("lololo: ", response_from_api)
        for line in response_from_api:
            question, answer = line.split(";")
            flashcard = {"question": question, "answer": answer}
            st.write("question: ", flashcard["question"], "  answer: ", flashcard["answer"])
            st.session_state.generated_flashcards.append(flashcard)

        if i == 0:
            break

    return st.session_state.generated_flashcards


def display_flashcard(index, flashcards, show_question):
    container = st.container(border=True)
    card = flashcards[index]
    if show_question:
        card_text = card["question"]
    else:
        card_text = card["answer"]
    container.write(card_text)

def interface_flashcards(flashcards):

    if len(flashcards) == 0:
        st.write("No flashcards available.")
    else:

        current_index = st.session_state.get("current_index", 0)
        show_question = st.session_state.get("show_question", True)

        # Display current flashcard
        display_flashcard(current_index, flashcards, show_question)

        # Button to toggle between question and answer
        if st.button("Show Answer" if show_question else "Show Question"):
            st.session_state.show_question = not show_question

        # Button to go to previous flashcard
        if current_index > 0:
            if st.button("Previous"):
                st.session_state.current_index -= 1

        # Button to go to next flashcard
        if current_index < len(flashcards) - 1:
            if st.button("Next"):
                st.session_state.current_index += 1


# Chatbot and flashcards generator from PDF

This application reads multiple PDFs and generates flashcards based on their content. It also provides a chatbot that answers user questions about the PDFs using Natural Language Processing.

### Demo
<img src="https://github.com/shmjade/PDF_FlashCards_Chatbot/blob/main/media/demo.gif" alt="Header"  width="1200"/>


**Technologies:**
- Langchain for Natural Language Processing 
- Streamlit for the graphical interface.
- OpenAI API to generate the flashcards and the chatbot answers.


### Running the project

1. Clone the repository
`git clone git@github.com:shmjade/PDF_FlashCards_Chatbot.git`

2. Obtain an [OpenAI API key](https://platform.openai.com/api-keys) and add it to the `.env` file in the project directory.



##### Configure environment
```shell
python3 -m venv pdf-venv            # create virtual environment
source pdf-venv/bin/activate        # activate 
pip install -r requirements.txt     # install packages
```


Configure virtual environment
`python3 -m venv pdf-venv`  
`source pdf-venv/bin/activate`
`pip install -r requirements.txt`


#### Sources
- [@alejandro-ao : ask-multiple-pdfs](https://github.com/alejandro-ao/ask-multiple-pdfs)
- [@PromtEngineer : Anki_Flash_Card_Generator](https://github.com/PromtEngineer/Anki_FlashCard_Generator/tree/main)
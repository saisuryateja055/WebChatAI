

# WebChatAI

## Overview
WebChatAI is an innovative chatbot that leverages the power of web scraping and retrieval-augmented generation (RAG) to provide dynamic responses based on user queries. Built using LangChain, Streamlit, BeautifulSoup for web scraping, and Pinecone for efficient data management, WebChatAI aims to deliver a seamless and informative interaction experience.

## Features
- **Dynamic Data Integration**: Utilizes BeautifulSoup to scrape data from web pages, ensuring that the chatbot always has the latest information at its disposal.
- **Advanced Natural Language Processing**: Employs LangChain and RAG for generating context-aware responses based on the scraped data.
- **Interactive Web Interface**: Built with Streamlit, WebChatAI offers a user-friendly interface that makes it easy for users to interact with the bot.
- **Efficient Data Handling**: Integrates Pinecone to manage the underlying data vectors, enhancing the speed and relevance of responses.

## Technologies Used
- **LangChain**: For leveraging advanced NLP models.
- **Retrieval-Augmented Generation (RAG)**: For generating responses using a hybrid of retrieval and generative methods.
- **Streamlit**: For creating the web interface.
- **BeautifulSoup**: For scraping data from web pages.
- **Pinecone**: For efficient vector database management.

## Installation
Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/saisuryateja055/WebChatAI.git
cd WebChatAI
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
Start the Streamlit web app:

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to interact with WebChatAI.

## How to Contribute
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Make sure to customize the installation and usage instructions based on your specific setup and environment configurations. This README structure provides a comprehensive guide for anyone interested in using or contributing to your project.

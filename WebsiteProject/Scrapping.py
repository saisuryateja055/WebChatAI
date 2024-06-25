from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import Anthropic
from langchain.chains import RetrievalQA
from langchain import PromptTemplate

import os
os.environ['ANTHROPIC_API_KEY']=''

os.environ['PINECONE_API_KEY']=''

def Scraped_data(url):
    loader = WebBaseLoader(url)
    data = loader.load()
    return data

def chunked_data(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_documents(data)
    return chunks

def vector_model(chunks):
    texts = [t.page_content for t in chunks]
    Embedding_model= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector = PineconeVectorStore.from_texts(texts, Embedding_model, index_name='youtube')
    return vector

def get_agent(vector):
    llm=Anthropic()
    retriever=vector.as_retriever()
    # Create Prompt
    template = """You are website bot that scrapes the webpage and answers the user queries
    Use the following pieces of context scrapped from url to answer the question at the end. be confident about answers 
  
    {context}


    Question: {question}
    Answer: 
    """

    prompt = PromptTemplate.from_template(template)

    agent=RetrievalQA.from_chain_type(llm=llm,retriever=retriever,chain_type='stuff')
    return agent

def Agent(url="https://medium.com/dataherald/how-to-langchain-sqlchain-c7342dd41614"):
    data=Scraped_data(url)
    chunks=chunked_data(data)
    print
    for ch in chunks:
        print(ch)
        print('-'*100)

    vector=vector_model(chunks)
    agent=get_agent(vector)
    return agent



agent=Agent()
res=agent.invoke("What is the number of house sold in march 2022 in Boston? ")
print(res)



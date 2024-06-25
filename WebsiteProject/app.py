import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage
from Scrapping import Agent
st.set_page_config(page_title='Website Chatting',page_icon='©',layout='wide')
st.title("Chat with Websites")
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL",value="")

if website_url is None or website_url == "":
    st.info("Please enter a valid website URL")


else:
    agent = Agent(website_url)
    # print(agent.invoke({"hi"))


    if "history" not in st.session_state:
        st.session_state.history=[
        AIMessage(content="How Can I help you...?")

    ]

    user_query=st.chat_input("Type your message here...")


    if user_query!='' and user_query is not None:
        response = agent.invoke({"query":user_query})
        print(response)
        st.session_state.history.append(HumanMessage(content=user_query))

        st.session_state.history.append(AIMessage(content=response['result']))




    for message in st.session_state.history:
        if isinstance(message,AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        if isinstance(message,HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)






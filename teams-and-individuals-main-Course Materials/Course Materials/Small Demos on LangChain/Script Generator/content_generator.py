import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from openai_callback import CustomOpenAICallback
from dotenv import load_dotenv
load_dotenv()

st.title("AI Content Writter")

template_title = PromptTemplate(
  template="You are good content generator. Generate one  engaging title for the given topic focused on {topic}",
  input_variables=['topic']
)

template_content = PromptTemplate(
  template="You are good content generator. Generate a  engaging content for the given title focused on {title}",
  input_variables=['title']
)


user_input  = st.text_input("Enter a topic")

#LLM
llm = OpenAI(temperature=0.9, verbose= True, callbacks=[CustomOpenAICallback()])

#Chains
title_chain = LLMChain(llm=llm, prompt=template_title, verbose= True,output_key='title')

content_chain = LLMChain(llm=llm, prompt=template_content, verbose= True,output_key='content')

sequential_chain = SequentialChain(chains=[title_chain,content_chain], input_variables=['topic'],output_variables=['title','content'])

if user_input: 
  with st.spinner('Please Wait...'):
    response = sequential_chain(user_input)
    st.write(response['title'])
    st.write(response['content'])
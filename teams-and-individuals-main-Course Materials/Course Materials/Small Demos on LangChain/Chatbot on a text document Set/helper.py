import os
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import streamlit as st

def get_pinecone_retriever():
    return Pinecone.from_existing_index(
        index_name=os.environ["INDEX_NAME"], embedding=OpenAIEmbeddings()
    )

import pinecone
def init_datastore(): 
  pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENV_REGION"],
    )


from typing import Set
def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string



def add_in_memory(question, answer):
     st.session_state['chat_history'].append((question, answer))




from langchain.chains import ConversationalRetrievalChain, RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from prompt_stuff import *

def get_answer(question):
    llm = ChatOpenAI(verbose=True)
    chain = ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    chain_type="stuff",
                    retriever=get_pinecone_retriever().as_retriever(),
                    return_source_documents=True,
                )
    
    with get_openai_callback() as cb:
      result = chain({"question": question, "chat_history": st.session_state['chat_history']})
      add_in_memory(question, result["answer"])
    return result, cb
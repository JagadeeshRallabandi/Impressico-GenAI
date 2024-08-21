import streamlit as st
from streamlit_chat import message
from helper import *
from dotenv import load_dotenv
#Load environment Variables
load_dotenv()

#Init Data Store
init_datastore()

#Create a cache
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "user_questions" not in st.session_state:
    st.session_state["user_questions"] = []

if "user_answers" not in st.session_state:
    st.session_state["user_answers"] = []

#User Interface
st.header("Documentation Helper Bot")
with st.form(key="QA", clear_on_submit=True):
    prompt = st.text_input(
        "Question",
        placeholder="Enter your question here..",
        key="et_question",
    )
    generate_answer = st.form_submit_button("Generate Answer")


if generate_answer:
    with st.spinner(f"Generating response for: {prompt}"):
        generated_response, cb = get_answer(prompt)
        print(cb)
        #Create Formatter response
        try:
            sources = set(
                [
                    doc.metadata["source"]
                    for doc in generated_response["source_documents"]
                ]
            )
            
            formatted_response = (
                f"{generated_response['answer']} \n\n {create_sources_string(sources)}"
            )
        except:
            formatted_response = f"{generated_response['answer']}"

        #Save Question and Answers
        st.session_state["user_questions"].insert(0, prompt)
        st.session_state["user_answers"].insert(0,formatted_response)


if st.session_state["user_answers"]:
    for index, (generated_response, user_query) in enumerate(
        zip(
            st.session_state["user_answers"],
            st.session_state["user_questions"],
        )
    ):
        message(user_query, is_user=True, key=index)
        message(generated_response)

import streamlit as st
from langchain.chat_models import ChatOpenAI
st.set_page_config(page_title="뭐든지 질문하세요~")
st.title('뭐든지 질문하세요~')

import os
import openai



def generate_response(input_text): #llm이 답변 생성
    llm = ChatOpenAI(temperature=0,
                     model_name='gpt-3.5-turbo',
                     )
    st.info(llm.predict(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'what types of text models does OpenAI provide?')
    submitted = st.form_submit_button('보내기')
    generate_response(text)

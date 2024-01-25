from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()


llm = ChatOpenAI()
output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 나이키 신발들을 평소신는 사이즈를 듣고 잘 맞는 사이즈를 추천해 줄 수 있는 사이즈 마스터야. 오프라인가서 신어보라는 이야기는 하지 말아줘"),
    ("user", "{input}")
])

chain = prompt | llm | output_parser

st.title("나이키 핏 마스터")
content = st.text_input('자주 신는 사이즈와 원하는 모델을 알려주세요.')

if st.button('사이즈 알아보기' , type="primary"):
    with st.spinner('사이즈를 알아보고 있어요...'):
        result = chain.invoke({"input": f"{content}. 내가 어떤 사이즈를 신으면 잘 맞을까?"})
        st.write(result)
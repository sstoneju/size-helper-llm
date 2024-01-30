from time import sleep
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4")
# llm = ChatOpenAI(model_name="gpt-3.5-turbo-instruct")

output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 아시아인이 신는 나이키 신발의 사이즈를 잘 아는 전문가야."),
    ("user", "{input}")
])

chain = prompt | llm | output_parser

st.title("나이키 핏 마스터")
customer_size = st.text_input('평소 신는 사이즈를 알려주세요.')
model_name = st.text_input('원하는 모델을 알려주세요.')
# model_name = st.text_input('발볼의 너비는 어떤 편인가요?')
fit_feel = st.radio(
    "어떤 착화감을 원하시나요?",
    ["약간 조이는 느낌", "딱 맞는 느낌", "쾌적한 느낌", "헐렁한 느낌"],
    index=None,
)

bind_messgae = f'나는 일반적으로 {customer_size} 사이즈의 신발을 신어. {fit_feel}으로 신발을 신는 것을 선호해. 그 경우 {model_name}의 Nike 모델을 신을 때는 몇 사이즈를 신으면 좋을까?'

if st.button('사이즈 알아보기' , type="primary"):
    with st.spinner('사이즈를 알아보고 있어요...'):
        result = chain.invoke({"input": bind_messgae})
        st.write(f'```{result}```')
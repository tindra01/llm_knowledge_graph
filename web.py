import streamlit as st
import json
import requests
import os
from streamlit_agraph import agraph, Node, Edge, Config, TripleStore
from chat import auto_knowledge_graph

st.title("⌨️ Knowledge Graph Generate")

st.markdown("### 문장이 구조도 설명")

user_text = st.text_area(label='문장을 적으세요 (10 ~ 5000자 제한)',
value = """지도 학습이란 레이블(Label) 이라는 정답과 함께 학습하는 것을 말한다.
자연어 처리는 대부분 지도 학습에 속한다.
레이블이라는 말 이외에도 y, 실제값 등으로 부르기도 한다.
간단히 말해 선생님이 문제를 내고 그 다음 바로 정답까지 같이 알려주는 방식의 학습 방법이다.
여러 문제와 답을 같이 학습함으로 미지의 문제에 대한 올바른 답을 예측하고자 하는 방법이다.
지도학습을 위한 데이터로는 문제와 함께 그 정답까지 같이 알고 있는 데이터가 선택된다.""", height=200)

res =  None
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('구조도 생성하기')
    if submitted:
        with st.spinner('구조도를 생성하는 중 입니다...'):
            result = auto_knowledge_graph(user_text)
            res = result
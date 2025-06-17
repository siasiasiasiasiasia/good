# app.py
import streamlit as st
import random

# 꿀팁 리스트
tips = [
    "전자레인지 청소는 레몬을 활용해 증기로 간단하게!",
    "별빛은 수백만 년 전에 발사된 것일 수 있어요.",
    "식초와 우유로 간단한 '우유 플라스틱'을 만들 수 있어요.",
    "탄산음료는 압력 변화로 기체가 빠져나오며 톡 쏘는 맛을 내요.",
    "지구의 물은 대부분 바닷물이고, 그중 97% 이상이 염수예요.",
    "구름은 물방울로 이루어져 있지만 매우 가볍게 떠 있어요.",
    "사람의 몸은 60% 이상이 물로 되어 있어요.",
    "달이 지구 주위를 도는 속도는 시간에 따라 변하고 있어요.",
]

# 페이지 설정
st.set_page_config(page_title="오늘의 과학 꿀팁", layout="wide")

# 기본 스타일
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #1d3557, #457b9d, #a8dadc);
            color: white;
        }

        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            margin-top: 2em;
            color: #ffffff;
        }

        .tip-box {
            margin-top: 2em;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 2em;
            border-radius: 20px;
            text-align: center;
            font-size: 1.5em;
        }

        .stButton > button {
            background-color: #f4a261;
            color: black;
            border-radius: 10px;
            padding: 10px 30px;
            font-size: 1.1em;
            margin: 1em auto;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<div class='title'>🌟 오늘의 과학 꿀팁 🌟</div>", unsafe_allow_html=True)

# 꿀팁 상태 초기화
if 'tip' not in st.session_state:
    st.session_state.tip = random.choice(tips)

# 꿀팁 표시
st.markdown(f"<div class='tip-box'>{st.session_state.tip}</div>", unsafe_allow_html=True)

# 버튼
if st.button("새 꿀팁 보기 🔁"):
    st.session_state.tip = random.choice(tips)
    st.experimental_rerun()

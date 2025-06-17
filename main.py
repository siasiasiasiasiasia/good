# app.py
import streamlit as st
import random

# 별이 반짝이는 CSS 효과
st.markdown("""
    <style>
    body {
        background-color: #000;
        color: white;
    }

    .starfield {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: black url('https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif') repeat;
        background-size: cover;
        opacity: 0.2;
    }

    .centered-title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        margin-top: 2em;
    }

    .tip-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2em;
        margin: 2em auto;
        width: 80%;
        font-size: 1.5em;
        text-align: center;
    }

    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        font-size: 1.2em;
        padding: 0.5em 2em;
        margin-top: 2em;
    }

    </style>
    <div class="starfield"></div>
""", unsafe_allow_html=True)

# 꿀팁 리스트
tips = [
    "전자레인지를 청소할 땐 레몬물을 데워 증기로 기름때를 쉽게 제거할 수 있어요!",
    "빛은 진공에서도 이동할 수 있지만 소리는 공기가 없으면 전달되지 않아요.",
    "우리가 보는 별빛은 수백만 년 전의 과거 모습일 수도 있어요.",
    "우유에 식초를 넣으면 카세인이 분리되어 플라스틱처럼 굳어요.",
    "중력은 모든 물체를 끌어당기지만, 질량이 클수록 힘도 세져요.",
    "탄산음료는 압력을 가하면 이산화탄소가 액체에 녹아있다가 뚜껑을 열면 기체로 빠져나와요.",
    "달은 지구의 공전에 영향을 주며 조수간만을 유발해요.",
    "사람의 몸속 물은 약 60% 이상이에요. 수분 섭취는 정말 중요해요!",
]

# 제목
st.markdown("<div class='centered-title'>✨ 오늘의 과학 꿀팁 ✨</div>", unsafe_allow_html=True)

# 꿀팁 보여주기
if 'tip' not in st.session_state:
    st.session_state.tip = random.choice(tips)

st.markdown(f"<div class='tip-box'>{st.session_state.tip}</div>", unsafe_allow_html=True)

# 버튼을 누르면 새로운 꿀팁
if st.button("새 꿀팁 보기 🔄"):
    st.session_state.tip = random.choice(tips)
    st.experimental_rerun()

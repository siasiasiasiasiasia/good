import streamlit as st
import random

# 배경 그라데이션 및 텍스트 스타일을 위한 CSS 삽입
st.markdown(
    """
    <style>
    /* 배경 그라데이션 */
    .stApp {
        background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
        min-height: 100vh;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 중앙 정렬된 컨테이너 박스 */
    .main-box {
        background: rgba(0, 0, 0, 0.5);
        padding: 2rem 3rem;
        border-radius: 12px;
        max-width: 600px;
        margin: 3rem auto;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
        text-align: center;
    }

    /* 버튼 스타일 */
    button[kind="primary"] {
        background-color: #00bcd4 !important;
        color: #000 !important;
        font-weight: 700 !important;
        padding: 0.7rem 1.5rem !important;
        border-radius: 10px !important;
        border: none !important;
        transition: background-color 0.3s ease !important;
    }
    button[kind="primary"]:hover {
        background-color: #0097a7 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.title("🔬 오늘의 과학 꿀팁")

tips = [
    "🍋 레몬과 베이킹 소다를 섞으면 친환경 청소제가 돼요. 주방 싱크대 청소에 딱!",
    "💡 LED 전구는 기존 전구보다 에너지 절약 효과가 크고 열도 적게 발생해요.",
    "🍎 사과를 자른 뒤 레몬즙을 바르면 갈변(갈색 변색)을 막을 수 있어요.",
    "🌿 실내 식물은 공기 정화뿐만 아니라 집중력 향상에도 도움을 줍니다.",
    "💧 얼음이 녹을 때 주변 온도가 내려가는 이유는 '흡열 반응' 때문이에요.",
    "🌞 햇빛을 받으면 우리 몸에서 비타민 D가 만들어져요. 하루 15분만 나가도 충분!",
    "🧊 얼음을 빨리 녹이려면 소금을 뿌려보세요. 소금물이 얼음의 녹는점을 낮춰서 빨리 녹아요.",
    "🍯 꿀은 천연 방부제 역할을 해요. 상처에 바르면 감염 예방에 도움됩니다.",
    "🔥 알루미늄 호일로 음식을 싸면 열이 고르게 분산되어 맛있게 데울 수 있어요.",
    "🌬️ 바람이 부는 방향은 기압 차이에 따른 현상으로, 간단한 날씨 예측에 활용돼요."
]

if st.button("오늘의 과학 꿀팁 받기"):
    tip = random.choice(tips)
    st.markdown(f"### {tip}")
else:
    st.write("버튼을 눌러 오늘의 신기한 과학 꿀팁을 받아보세요! 😊")

st.markdown('</div>', unsafe_allow_html=True)

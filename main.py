import streamlit as st
import random

# CSS로 배경, 별 애니메이션, 텍스트 박스 꾸미기
st.markdown(
    """
    <style>
    /* 배경 이미지와 전체 스타일 */
    body {
        background-image: url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-attachment: fixed;
        color: #e0f7fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 반짝이는 별 애니메이션 */
    @keyframes twinkle {
        0%, 100% {opacity: 1;}
        50% {opacity: 0.5;}
    }

    .star {
        position: fixed;
        width: 2px;
        height: 2px;
        background: white;
        border-radius: 50%;
        animation: twinkle 2s infinite ease-in-out;
    }

    /* 별 여러개 위치 지정 */
    .star:nth-child(1) {top: 10%; left: 20%; animation-delay: 0s;}
    .star:nth-child(2) {top: 30%; left: 80%; animation-delay: 1s;}
    .star:nth-child(3) {top: 50%; left: 40%; animation-delay: 1.5s;}
    .star:nth-child(4) {top: 70%; left: 60%; animation-delay: 0.5s;}
    .star:nth-child(5) {top: 85%; left: 25%; animation-delay: 1.2s;}

    /* 본문 박스 스타일 */
    .main-content {
        background: rgba(0, 0, 50, 0.6);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 0 20px #00bcd4;
        max-width: 600px;
        margin: 3rem auto;
        text-align: center;
    }

    button {
        background-color: #00acc1;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1.5rem;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #00838f;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 별 div 추가 (fixed 위치라 어디서든 보임)
st.markdown(
    """
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    """,
    unsafe_allow_html=True
)

# 본문 시작
st.markdown('<div class="main-content">', unsafe_allow_html=True)
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

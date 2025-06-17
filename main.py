import streamlit as st
import random

st.title("🧪 분자 결합 퀴즈 게임")

# 원소와 그들의 가능한 화합물 (분자식: 원소 구성)
compound_dict = {
    "물 (H₂O)": {"H": 2, "O": 1},
    "이산화탄소 (CO₂)": {"C": 1, "O": 2},
    "암모니아 (NH₃)": {"N": 1, "H": 3},
    "메탄 (CH₄)": {"C": 1, "H": 4},
    "산소 (O₂)": {"O": 2},
    "질소 (N₂)": {"N": 2},
    "염화수소 (HCl)": {"H": 1, "Cl": 1},
}

elements = ["H", "O", "C", "N", "Cl"]

if "score" not in st.session_state:
    st.session_state.score = 0

def generate_question():
    compound_name, composition = random.choice(list(compound_dict.items()))
    return compound_name, composition

if "current_question" not in st.session_state:
    st.session_state.current_question = generate_question()

compound_name, composition = st.session_state.current_question

st.write(f"### 어떤 원소들을 조합해서 **{compound_name}** 을(를) 만들 수 있을까?")

st.write("아래에서 원소를 선택하고, 각각 몇 개가 필요한지 입력하세요.")

selected_elements = {}
for elem in elements:
    count = st.number_input(f"{elem} 개수", min_value=0, max_value=10, value=0, key=elem)
    selected_elements[elem] = count

if st.button("제출"):
    correct = True
    for elem, required_count in composition.items():
        if selected_elements.get(elem, 0) != required_count:
            correct = False
            break
    # 추가로, 선택한 원소 중 필요하지 않은 게 있으면 틀림
    for elem, cnt in selected_elements.items():
        if cnt != 0 and elem not in composition:
            correct = False
            break

    if correct:
        st.success("🎉 정답입니다!")
        st.session_state.score += 1
        st.write(f"현재 점수: {st.session_state.score}")
        st.session_state.current_question = generate_question()
    else:
        st.error("😢 틀렸어요! 다시 시도해보세요.")
        # 힌트 출력
        hint = ", ".join([f"{k}: {v}" for k, v in composition.items()])
        st.info(f"힌트: 필요한 원소와 개수는 {hint} 입니다.")

st.write(f"현재 점수: {st.session_state.score}")


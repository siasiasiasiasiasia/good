import streamlit as st

st.title("🔍 물건 속 화학 원소 탐색기")

st.write("물건 이름을 입력하면 그 안에 들어있는 주요 화학 원소들을 알려드려요!")

# 간단한 예시 데이터베이스 (물건 : 포함된 원소 리스트)
item_elements = {
    "물": ["H", "O"],
    "소금": ["Na", "Cl"],
    "설탕": ["C", "H", "O"],
    "철": ["Fe"],
    "알루미늄 캔": ["Al"],
    "유리": ["Si", "O", "Na", "Ca"],
    "에탄올": ["C", "H", "O"],
    "황산": ["H", "S", "O"],
    "산소통": ["O"],
    "황": ["S"]
}

item = st.text_input("물건 이름을 입력하세요 (예: 물, 소금, 설탕)")

if item:
    item_lower = item.strip().lower()
    found = False
    for key in item_elements.keys():
        if item_lower == key.lower():
            st.write(f"**{key}** 에 포함된 화학 원소:")
            st.write(", ".join(item_elements[key]))
            found = True
            break
    if not found:
        st.warning("해당 물건에 대한 데이터가 없습니다. 다른 물건 이름으로 시도해보세요!")

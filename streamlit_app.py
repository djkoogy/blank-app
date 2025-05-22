import streamlit as st

# --- 사이드바 (슬라이더) ---
st.sidebar.title("슬라이더")
slider_val = st.sidebar.slider("값 선택", 0, 100, 50)

# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["탭 01", "탭 02", "탭 03"])

with tab1:
    st.write("탭 01 내용")

    # 2x2 레이아웃 구성
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧱 레이아웃 01")
        st.info(f"슬라이더 값: {slider_val}")
    with col2:
        st.markdown("### 🧱 레이아웃 02")
        st.success("오른쪽 상단 영역")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🧱 레이아웃 03")
        st.warning("왼쪽 하단 영역")
    with col4:
        st.markdown("### 🧱 레이아웃 04")
        st.error("오른쪽 하단 영역")

with tab2:
    st.write("탭 02 내용")
    
  
    import datetime
    name = st.text_input("이름을 입력하세요")
    age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
    birthdate = st.date_input("생년월일 선택")
    hobby = st.selectbox("취미 선택", ["독서", "운동", "게임", "음악"])
    agree = st.checkbox("이용 약관에 동의합니다")
    file = st.file_uploader("파일 업로드")


    if st.button("제출"):
        st.success(f"{name}님({age}세), 제출 완료!")
        st.markdown("### 📋 입력 결과")
        st.write(f"🙋 이름: {name}")
        st.write(f"🎂 나이: {age}세")
        st.write(f"📅 생일: {birthdate}")
        st.write(f"🎨 당신의 취미는 : {hobby}")


with tab3:
    st.write("탭 03 내용")

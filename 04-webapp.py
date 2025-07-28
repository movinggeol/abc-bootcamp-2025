import streamlit as st
from ai import get_personality_analysis
from dotenv import load_dotenv

load_dotenv()

st.title("AI 관상 보기 프로그램")
st.write("---")

st.write("안녕하세요! AI 관상가입니다.")
st.write("당신의 얼굴 특징을 알려주시면 성격과 미래를 분석해드릴게요.")

face_desc = st.text_area(
    "얼굴 특징을 입력하세요 : ", placeholder="예시 : 둥근 얼굴, 큰 눈, 높은 코, 두꺼운 입술 등",
    height=100
)
face_desc = face_desc.strip()

if st.button("관상 보기", type="primary"): # '버튼이 클릭되었음'에 대한 조건문
    if face_desc: # '문자열 있음'에 대한 조건문 (strip()으로 인해 좌우 공백이 제거되므로, 공백 제외 문자 존재 유무)
        with st.spinner("관상을 분석 중입니다..."):
            result = get_personality_analysis(face_desc)
            st.write("----")
            st.write("관상 분석이 끝났습니다.")
            st.info(result)
        # with 구문이 끝나기 전까지는 코드 수행 중임을 알려주는 
    else:
        st.warning("얼굴 특징을 입력하고, 관상보기 버튼을 클릭해주세요") # st.error 비슷한 기능
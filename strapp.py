import streamlit as st
import pandas as pd 

# Title of the app (타이틀 크기 줄이기)
st.markdown("<h2 style='text-align: center;'>쓰레기통 위치 안내 시스템</h2>", unsafe_allow_html=True)

# Display a message about the trash can proximity with larger font size and colored text
st.markdown("<h1 style='color:rgb(38, 91, 188); text-align: center;'>🚶‍♂️ 도보 10분 이내에 쓰레기통이 있습니다!</h1>", unsafe_allow_html=True)

# Display additional info
st.info("당신의 작은 행동이 지구온난화를 막는 데에 큰 도움이 됩니다. 😊")

st.info("'우리 동네 개선 프로젝트'를 시행하고 있는 두정고등학교 3학년 학생입니다. 노태산의 입구와 산행길 중간에 쓰레기통을 설치하였으니 관심 가져주시면 감사하겠습니다!")

# 데이터 준비
data = {
    "Year": ["1993~2002", "2003~2012", "2013~2022"],
    "Sea  (cm)": [2.87, 6.51, 10.22]
}

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# 인덱스를 'Year'로 설정
df.set_index('Year', inplace=True)

# 앱 타이틀
st.title("해수면 상승 변화")
st.markdown("더이상 먼 나라의 이야기가 아닙니다. 해마다 부산의 바다는 높아지고 있습니다.")

# 그래프 그리기
st.line_chart(df)

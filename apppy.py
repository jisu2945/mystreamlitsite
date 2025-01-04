import streamlit as st

# Step 2: Create Streamlit Web App
def streamlit_app():
    # Title of the app
    st.title("쓰레기통 위치 안내 시스템")

    # Display a message about the trash can proximity (using emojis as Unicode)
    st.write("🚶‍♂️ 도보 10분 이내에 쓰레기통이 있습니다!")

    # Display additional info
    st.info("작은 당신의 행동이 지구온난화를 늦출 수 있습니다. 😊")

# Call the function to run the Streamlit app
if __name__ == "__main__":
    streamlit_app()


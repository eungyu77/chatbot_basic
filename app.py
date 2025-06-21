import streamlit as st
import os
from dotenv import load_dotenv

# 기본 모델 리스트
MODEL_OPTIONS = [
    "gpt-3.5-turbo",
    "gpt-4.1",
    "gpt-4o",
    # 필요한 경우 다른 모델을 추가
]
with st.sidebar:
    selected = st.selectbox("사용할 모델 선택", MODEL_OPTIONS)
    
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("KEY가 없습니다. .env 파일을 확인하세요.")
    st.stop()
    
st.title("내 챗봇")
from openai import OpenAI
client = OpenAI(api_key = OPENAI_API_KEY)

if "openai_model" not in st.session_state:
    st.session_state.openai_model = selected
else:
    st.session_state.openai_model = selected
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.chat_message("assistant").markdown("안녕하세요! 무엇을 도와드릴까요?")
    # 2. messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
user_input = st.chat_input(" .", key="chat_input")   

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({
        "role":"user", "content":user_input
    })
    with st.chat_message("assistant"):
        with st.spinner("응답을 생성하는 중..."):
            message_placeholder=st.empty()
            full_response = ""
            
            response = client.chat.completions.create(
                model = st.session_state.openai_model,
                messages = st.session_state.messages,
                stream = True
            )
            
            for chunk in response :
                if hasattr(chunk.choices[0].delta, "content"):
                    content = chunk.choices[0].delta.content
                    if content is not None:
                        full_response += content
                    message_placeholder.markdown(full_response + "▍")
            message_placeholder.markdown(full_response)
    st.session_state.messages.append({
        "role":"assistant", "content":full_response
    })
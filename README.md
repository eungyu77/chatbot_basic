# 새 프로젝트 만들기
0. 이 폴더의 이름을 MyProject 가 아닌 다른 이름으로 변경한다.

1. 가상환경을 생성한다.
```powershell
python -m venv myvvenv
```

2. 가상환경을 활성화한다.
```powershell
myvenv/Scripts/activate
```

3. Github 에 업로드 하기위해 현재 폴더를 git 환경으로 만든다.
```powershell
git init
```

4. Github Desktop 에서 현재 폴더를 Local Repository 형태로 열기 한다.

5. commit message 에 아무 메시지나 입력한다. 
예) 첫 업로드

6. commit 버튼을 누른다.

7. publish 버튼을 누른다.

8. vscode 의 터미널에서 streamlit 라이브러리를 설치한다.
```powershell
pip install streamlit
pip install dotenv
```

9. requirements.txt 파일을 만든다.
```txt
streamlit
dotenv
openai
```

10. app.py 파일을 만든다.
```python
import streamlit as st

st.chat_input("채팅을 입력하세요.", key="chat_input")
```

11. 서버를 실행한다.
```powershell
streamlit run app.py
```
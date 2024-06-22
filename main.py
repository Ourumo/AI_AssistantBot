import openai # openai
import os
from langchain_openai import ChatOpenAI # langchain_openai
from dotenv import load_dotenv # env 로드
import getpass
import subprocess # 터미널 사용

# 최초 로그인 시, API_Key 입력
with open('.env', 'r') as env:
    key = env.read()
    key = key.replace("OPENAI_API_KEY=", "")
if(key == ""):
    key = getpass.getpass(prompt="API키를 입력해주세요: ")
    with open('.env', 'w') as env:
        env.write(f"OPENAI_API_KEY={key}")
print(key)


# 가능하다면 프로그램을 띄우는 느낌? -> PyInstaller
# langchain_openai를 이용해서 gpt-3.5-turbo 사용
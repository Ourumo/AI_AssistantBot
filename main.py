import openai # openai
from langchain_openai import ChatOpenAI # langchain_openai
from dotenv import load_dotenv # env 로드
import subprocess # 터미널 사용

load_dotenv()

with open('prompt.txt', 'r') as file:
    prompt = file.read()
print(prompt)

# 가능하다면 프로그램을 띄우는 느낌?
# langchain_openai를 이용해서 gpt-3.5-turbo 사용
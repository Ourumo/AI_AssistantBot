import openai # openai
import os
from langchain import LLMChain, PromptTemplate # langchain
from langchain_openai import ChatOpenAI # langchain_openai
from dotenv import load_dotenv # env 로드
import getpass
import subprocess # 터미널 사용

load_dotenv()

with open('prompt.txt', 'r') as file:
    prompt = file.read()
    print(prompt)

# getpass 사용해서 최초실행 비번 입력 방식
#with open('.env', 'r') as env:
#    key = env.read()
#    print(key)
#api_key = getpass.getpass(prompt="Enter your OpenAI API key: ")
#os.environ["OPENAI_API_KEY"] = api_key
    
#chat = ChatOpenAI(model="gpt-3.5-turbo")

#template = PromptTemplate(input_variables=["question"], template="Q: {question}\nA:")

#llm_chain = LLMChain(llm=chat, prompt=template)

#response = llm_chain.run({"question": "LangChain을 사용하여 OpenAI와 대화하는 방법은?"})

#print(response)


# 가능하다면 프로그램을 띄우는 느낌? -> PyInstaller
# langchain_openai를 이용해서 gpt-3.5-turbo 사용
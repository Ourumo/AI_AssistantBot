from getpass import getpass
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 최초 로그인 시, API_Key 입력
with open('.env', 'r') as env:
    key = env.read()
    key = key.replace("OPENAI_API_KEY=", "")
if(key == ""):
    key = getpass(prompt="API키를 입력해주세요: ")
    with open('.env', 'w') as env:
        env.write(f"OPENAI_API_KEY={key}")

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    #("human", "hello!!")
])

response = model.invoke(input="hello!!")

print(response.content)


# chain??
# 가능하다면 프로그램을 띄우는 느낌? -> PyInstaller
# langchain_openai를 이용해서 gpt-3.5-turbo 사용
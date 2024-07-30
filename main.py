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

#prompt = ChatPromptTemplate.from_messages([
#    ("human", "hello!!")
#])s
#output_parser = StrOutputParser()
#chain = prompt | model | output_parser
#chain.invoke({"input": "hello!!"})

# chain??
# 가능하다면 프로그램을 띄우는 느낌? -> PyInstaller
# langchain_openai를 이용해서 gpt-3.5-turbo 사용
# langchain
#1. 특정 앱 실행
#   “XX 디렉토리에 있는 YY 실행”
#	기본적으로 applications에 접근
#2. pdf 번역
#	“XX 디렉토리에 있는 YY 번역해줘”
#	XX 디렉토리에 YY.txt 파일로 저장
#3. 특정 텍스트를 복사
#	“YY에 대한 답변을 클립보드에 복사해줘”
#	질문에 대한 답변을 출력하지 않고 저장
#4. 질문에 대한 대답 생성
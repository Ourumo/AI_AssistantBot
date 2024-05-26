import gradio as gr
from openai import OpenAI
import pyaudio
import wave
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system = """
    
"""

def Process(prompt, history):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

def Record() -> str:
    # PyAudio 객체 생성
    p = pyaudio.PyAudio()

    # 오디오 스트림 설정
    FORMAT = pyaudio.paInt16 # 오디오 포맷
    CHANNELS = 1 # 채널 수
    RATE = 44100 # 샘플링 레이트 (Hz)
    CHUNK = 1024 # 청크 크기 (버퍼 크기)
    RECORD_SECONDS = 5 # 녹음 시간 (초)
    OUTPUT_FILENAME = "output.wav" # 출력 파일 이름

    # 입력 스트림 열기
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("녹음 시작")

    frames = []

    # 데이터를 읽고 저장
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("녹음 끝")
    
    # 스트림 정리
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Wave 파일로 저장
    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    audio_file = open("./output.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    return transcription.text

def Speak(chatbot) -> None:
    # chatbot = [[res, req], ...]
    text = chatbot[-1][1]
    if (text == None):
        return
    
    # PyAudio 객체 생성
    p = pyaudio.PyAudio()

    # 오디오 스트림 설정
    FORMAT = pyaudio.paInt16 # 오디오 포맷
    CHANNELS = 1 # 채널 수
    RATE = 24000 # 샘플링 레이트 (Hz)
    CHUNK = 512 # 청크 크기 (버퍼 크기)

    # 입력 스트림 열기
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        response_format="pcm",
        input=text,
        speed='1.2'
    ) as response:
        for chunk in response.iter_bytes(chunk_size=CHUNK):
            stream.write(chunk)
    
with gr.Blocks() as demo:
    chat = gr.ChatInterface(fn=Process)
    btn = gr.Button('음성 인식')
    btn.click(fn=Record, outputs=chat.textbox)
    chat.chatbot.change(fn=Speak, inputs=chat.chatbot)
    
if __name__ == "__main__":
    demo.launch()
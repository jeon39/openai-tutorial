import os

import dotenv
import openai
from dotenv import load_dotenv

dotenv.load_dotenv()
#openai.organization = "org-udpJLYQeRnOltmhB05uT4rwe"
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

# dotenv로 환경변수 빼고, 아래 코드를 사용하지 않음
#assert os.getenv('OPENAI_API_KEY') is None
#openai.api_key = os.getenv("OPENAI_API_KEY", "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")
#modeles = openai.Model.list()
#print(modeles)

response = openai.Completion.create(
    model="text-davinci-003",
    #prompt="My name is VAN. \n\nQ: What's your name?\nA:",
    prompt="Q: 그럼 너의 주민번호 앞자리는 무엇이니?\nA:",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response)

print(response.choices[0].text)

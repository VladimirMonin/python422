"""
1. Установите бибилотеку openai
pip install openai

2. Из vsegpt - возьмите ключик
3. 
"""

from openai import OpenAI

client = OpenAI(
    api_key="ВВЕДИТЕ ВАШ КЛЮЧ", # ваш ключ в VseGPT после регистрации
    base_url="https://api.vsegpt.ru/v1",
)

prompt = "Напиши 5 прикольных шуток про Python разработчиков которые будут смешные для русскоговорящих жителей СНГ"

messages = []
#messages.append({"role": "system", "content": system_text})
messages.append({"role": "user", "content": prompt})

response_big = client.chat.completions.create(
    model="openai/gpt-4o-mini", # id модели из списка моделей - можно использовать OpenAI, Anthropic и пр. меняя только этот параметр
    messages=messages,
    temperature=1.3,
    n=1,
    max_tokens=4000, # максимальное число ВЫХОДНЫХ токенов. Для большинства моделей не должно превышать 4096

)

#print("Response BIG:",response_big)
response = response_big.choices[0].message.content
print("Ответ:",response)
"""
1. Установите бибилотеку openai
pip install openai

2. Из vsegpt - возьмите ключик
3. 
"""

from dataclasses import dataclass
from openai import OpenAI
from typing import Optional

@dataclass
class OpenAISettings:
    api_key: str = "sk-or-vv-32acad84830483432df6bb1eb3114ede486fe620ba237c07f152b84c6a27e782"
    base_url: str = "https://api.vsegpt.ru/v1"
    model: str = "openai/gpt-4o-mini"
    temperature: float = 1.0
    max_tokens: int = 100

class OpenAIRequester:
    def __init__(self, settings: OpenAISettings):
        self.settings = settings
        self.client = OpenAI(
            api_key=settings.api_key,
            base_url=settings.base_url
        )
    
    def __call__(self, prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        
        response = self.client.chat.completions.create(
            model=self.settings.model,
            messages=messages,
            temperature=self.settings.temperature,
            n=1,
            max_tokens=self.settings.max_tokens
        )
        
        return response.choices[0].message.content

class OpenAIFacade:
    def __init__(self, settings: Optional[OpenAISettings] = None):
        self.settings = settings or OpenAISettings()
        self.requester = OpenAIRequester(self.settings)
    
    def run(self, prompt: str, history: list|None = None):

        if history:
            prompt = '\n'.join(history) + '\n' + prompt
        response = self.requester(prompt)
        return response

if __name__ == "__main__":
    facade = OpenAIFacade()
    history = []
    while True:
        prompt = input("Запрос: ")
        response = facade.run(prompt, history)
        print(response)
        print('-----------------------------------')
        history.append(response)
    


# # Базовое использование
# facade = OpenAIFacade()
# facade.run()

# # С кастомными настройками
# custom_settings = OpenAISettings(
#     temperature=0.7,
#     max_tokens=2000
# )
# facade = OpenAIFacade(custom_settings)
# facade.run()

# # Использование только requester
# settings = OpenAISettings()
# requester = OpenAIRequester(settings)
# response = requester("Расскажи анекдот")
# print(response)

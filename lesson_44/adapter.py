"""
Lesson 44: Adapter


"""
from abc import ABC, abstractmethod

class AbstractAIAdapter(ABC):
    """Абстрактный класс для адаптеров AI сервисов"""
    
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass

class AnthropicAPI:
    """Имитация API Anthropic"""
    
    def create_completion(self, prompt: str) -> dict:
        print(f"[Anthropic API] Получил запрос: {prompt}")
        return {
            "completion": f"Anthropic ответ на: {prompt}",
            "stop_reason": "complete"
        }

class OpenAIAPI:
    """Имитация API OpenAI"""
    
    def chat_completion(self, messages: list) -> dict:
        prompt = messages[-1]['content']
        print(f"[OpenAI API] Получил запрос: {prompt}")
        return {
            "choices": [{
                "message": {"content": f"OpenAI ответ на: {prompt}"}
            }]
        }

class AnthropicAdapter(AbstractAIAdapter):
    """Адаптер для Anthropic API"""
    
    def __init__(self, anthropic_api: AnthropicAPI):
        print("[Anthropic Adapter] Инициализация")
        self.api = anthropic_api

    def generate_text(self, prompt: str) -> str:
        print("[Anthropic Adapter] Адаптирую запрос")
        response = self.api.create_completion(prompt)
        result = response["completion"]
        print(f"[Anthropic Adapter] Адаптировал ответ: {result}")
        return result

class OpenAIAdapter(AbstractAIAdapter):
    """Адаптер для OpenAI API"""
    
    def __init__(self, openai_api: OpenAIAPI):
        print("[OpenAI Adapter] Инициализация")
        self.api = openai_api

    def generate_text(self, prompt: str) -> str:
        print("[OpenAI Adapter] Адаптирую запрос")
        messages = [{"role": "user", "content": prompt}]
        response = self.api.chat_completion(messages)
        result = response["choices"][0]["message"]["content"]
        print(f"[OpenAI Adapter] Адаптировал ответ: {result}")
        return result

def process_with_ai(ai_adapter: AbstractAIAdapter, prompt: str):
    print(f"\n[Клиент] Отправляю запрос: {prompt}")
    response = ai_adapter.generate_text(prompt)
    print(f"[Клиент] Получил ответ: {response}\n")

def main():
    # Создаем экземпляры API и адаптеров
    anthropic = AnthropicAdapter(AnthropicAPI())
    openai = OpenAIAdapter(OpenAIAPI())
    
    # Используем оба API через единый интерфейс
    prompt = "Расскажи о паттерне Адаптер"
    
    process_with_ai(anthropic, prompt)
    process_with_ai(openai, prompt)

if __name__ == "__main__":
    main()

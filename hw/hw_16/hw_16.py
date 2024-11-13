from abc import ABC, abstractmethod
import os
import shutil
import zipfile
import rarfile
import py7zr
from dataclasses import dataclass
from openai import OpenAI
from typing import Any

@dataclass
class ProcessorConfig:
    api_provider: str
    api_key: str
    base_url: str
    model: str
    temperature: float = 0.7

class AIStrategy(ABC):
    @abstractmethod
    def process_request(self, prompt: str, data: str) -> str:
        pass

class OpenAIStrategy(AIStrategy):
    def __init__(self, config: ProcessorConfig):
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url
        )
        self.model = config.model
        self.temperature = config.temperature
    
    def process_request(self, prompt: str, data: str) -> str:
        messages = [
            {"role": "system", "content": "Вы являетесь полезным рецензентом кода."},
            {"role": "user", "content": f"{prompt}\n\nCode to review:\n{data}"}
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature
        )
        return response.choices[0].message.content

class ProcessingState(ABC):
    @abstractmethod
    def process(self, context: 'ProcessingContext', data: Any, ai_strategy: AIStrategy) -> None:
        pass

class UnpackState(ProcessingState):
    def __init__(self, target_dir: str):
        self.target_dir = target_dir

    def process(self, context: 'ProcessingContext', archive_path: str, ai_strategy: AIStrategy):
        file_name = os.path.basename(archive_path)
        extract_dir = os.path.join(os.path.dirname(archive_path), self.target_dir)
        
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
        elif archive_path.endswith('.rar'):
            with rarfile.RarFile(archive_path, 'r') as rar_ref:
                rar_ref.extractall(extract_dir)
        elif archive_path.endswith('.7z'):
            with py7zr.SevenZipFile(archive_path, 'r') as sz_ref:
                sz_ref.extractall(extract_dir)
                
        context.data = extract_dir

class AICheckState(ProcessingState):
    def __init__(self, prompt: str):
        self.prompt = prompt
        
    def process(self, context: 'ProcessingContext', extract_dir: str, ai_strategy: AIStrategy):
        code_content = ""
        for root, _, files in os.walk(extract_dir):
            for file in files:
                if file.endswith(('.py', '.js', '.html', '.css', '.sql')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_content += f"\nFile: {file}\n{f.read()}\n"
        
        context.results = ai_strategy.process_request(self.prompt, code_content)

class ReportState(ProcessingState):
    def __init__(self, format: str = 'md'):
        self.format = format
        
    def process(self, context: 'ProcessingContext', data: str, ai_strategy: AIStrategy):
        report_path = os.path.join(os.path.dirname(context.archive_path), f"review_report.{self.format}")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Отчет по коду\n\n{context.results}")
        
        # Очистка временной директории
        shutil.rmtree(data)

class ProcessingContext:
    def __init__(self):
        self.state: ProcessingState = None
        self.data: Any = None
        self.results: Any = None
        self.archive_path: str = None
        
    def process(self, data: Any, ai_strategy: AIStrategy):
        self.state.process(self, data, ai_strategy)

class AIProcessorFacade:
    def __init__(self, ai_strategy: AIStrategy):
        self.ai_strategy = ai_strategy
        self.context = ProcessingContext()
        
    def process_homework(self, archive_path: str):
        self.context.archive_path = archive_path
        
        # Распаковка архива
        self.context.state = UnpackState(target_dir="temp_homework")
        self.context.process(archive_path, self.ai_strategy)
        
        # Проверка кода через ИИ
        self.context.state = AICheckState(
            prompt="Проверьте этот код. Проверьте: 1) Стиль кода 2) Потенциальные ошибки 3) Проблемы производительности 4) Проблемы безопасности. Предоставьте конкретные рекомендации по улучшению."
        )
        self.context.process(self.context.data, self.ai_strategy)
        
        # Генерация отчета
        self.context.state = ReportState(format="md")
        self.context.process(self.context.data, self.ai_strategy)

def main():
    # Конфигурация для AI
    config = ProcessorConfig(
        api_provider="openai",
        api_key="sk-or-vv-32acad84830483432df6bb1eb3114ede486fe620ba237c07f152b84c6a27e782",
        base_url="https://api.vsegpt.ru/v1",
        model="anthropic/claude-3-haiku",
        temperature=0.7
    )
    
    # Создание стратегии и процессора
    ai_strategy = OpenAIStrategy(config)
    processor = AIProcessorFacade(ai_strategy)
    
    # Запрос пути к архиву
    archive_path = input("Введите путь к архиву с домашним заданием: ").strip('"').strip("'")
    
    try:
        processor.process_homework(archive_path)
        print(f"Проверка завершена. Отчет сохранен в {os.path.dirname(archive_path)}/review_report.md")
    except Exception as e:
        print(f"Произошла ошибка при обработке: {str(e)}")
    
    input("Нажмите Enter для выхода...")

if __name__ == "__main__":
    main()

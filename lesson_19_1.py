message = "Hello, I'm lesson_19_1.py"

# При запуске этого файла напрямую
# __name__ = __main__
# При импорте в другой файл
# __name__ = lesson_19_1
# print(__name__)

def get_message():
    print(message)

if __name__ == "__main__":
    get_message()

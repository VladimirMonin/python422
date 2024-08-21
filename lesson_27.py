"""
Lesson 27
Typing - модуль для сложной, детальной аннотации типов
"""
from typing import List, Dict, Tuple, Set, Union, Optional
# Аннотации типов с указанием типов данных в коллекциях

"""
List[int] - список целых чисел
List[Optional[int]] - список целых чисел или None
List[Union[int, str]] - список целых чисел или строк

Dict[str, int] - словарь, где ключи - строки, а значения - целые числа
Dict[str, Union[int, str]] - словарь, где ключи - строки, а значения - целые числа или строки
"""
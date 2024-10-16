"""
Lesson 40
Магическиее методы 
1. __call__
2. __bool__
3. __len__
"""

class File:
    def __init__(self, path):
        self.path = path

    def __bool__(self):
        return bool(self.path)


file = File('')

if file
    print('Всегда да')
else:
    print('нет')
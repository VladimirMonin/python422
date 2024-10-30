from copy import deepcopy

class ColorPrototype:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def clone(self):
        return deepcopy(self)

red = ColorPrototype("Red", 255, 0, 0)
green = ColorPrototype("Green", 0, 255, 0)

another_red = red.clone()
another_red.name = "Another Red"
another_green = green.clone()

print(red)          # Output: Red (255, 0, 0)
print(another_red)  # Output: Another Red (255, 0, 0)
print(green)        # Output: Green (0, 255, 0)


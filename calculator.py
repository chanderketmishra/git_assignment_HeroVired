import math

class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            return "Error"
        return a / b

    def square_root(self, x):
        return math.sqrt(x)

print("Calculator Ready")

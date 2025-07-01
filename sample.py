class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(f"Adding {self.a} + {self.b}")
        return self.a + self.b

    def subtract(self):
        print(f"Subtracting {self.a} - {self.b}")
        return self.a - self.b

    def multiply(self):
        print(f"Multiplying {self.a} * {self.b}")
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        print(f"Dividing {self.a} / {self.b}")
        return self.a / self.b


# Example usage
if __name__ == "__main__":
    calc = Calculator(10, 5)
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())

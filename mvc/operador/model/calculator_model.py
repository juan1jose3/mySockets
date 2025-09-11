class CalculatorModel:
    def calculate(self, a, b, operation):
        if operation == "sum":
            return a + b
        elif operation == "subtract":
            return a - b
        else:
            return "Unknown operation"

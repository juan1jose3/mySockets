class ConsoleView:
    def get_input(self):
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))
        op = input("Enter operation (sum/subtract): ").strip().lower()
        return a, b, op

    def show_result(self, result):
        print(f"Result from operator: {result}")

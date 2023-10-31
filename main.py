class Calculator:
    """
    This is a Calculator class which provides basic arithmetic operations like addition, subtraction, multiplication and division.
    """
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

def main():
    calculator = Calculator()

    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                result = calculator.add(num1, num2)
            elif user_input == "subtract":
                result = calculator.subtract(num1, num2)
            elif user_input == "multiply":
                result = calculator.multiply(num1, num2)
            elif user_input == "divide":
                result = calculator.divide(num1, num2)

            print("Result: {}".format(result))
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

def main():
    def firstFunction():
        print("Hello World!")
        
    def secondFunction():
        num1 = int(input("Enter Number 1: "))
        while True:
            try:
                num2 = int(input("Enter Number 2: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        addVal = num1 + num2
        subVal = num1 - num2
        multiVal = num1 * num2
        divVal = num1 / num2
        
        print(f"Addition = {addVal}")
        print(f"Subtraction = {subVal}")
        print(f"Multiplication = {multiVal}")
        print(f"Division = {divVal}")
        
    firstFunction()
    secondFunction()

if __name__ == "__main__":
    main()

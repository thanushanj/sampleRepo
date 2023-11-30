def main():
    def firstFunction():
        print("Hello Youtube!!")
        
    def secondFunction():
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        
        addVal = num1 + num2
        subVal = num1 - num2
        multiVal = num1 * num2
        divVal = num1 / num2
        
        print("Addition =", addVal)
        print("Subtract =", subVal)
        print("Multiplication =", multiVal)
        print("Division =", divVal)
        
    firstFunction()
    secondFunction()

if __name__ == "__main__":
    main()

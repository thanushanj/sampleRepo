def main():
    def firstFunction():
        print("Hello GitHub!")
        
    def secondFunction():
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        
        addVal = num1 + num2
        multiVal = num1 * num2
        
        print("Addition =", addVal)
        print("Multiplication =", multiVal)
        
    firstFunction()
    secondFunction()

if __name__ == "__main__":
    main()

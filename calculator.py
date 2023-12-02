def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
    
def calculator():
    while True:
        
        print("\t             Simple Calculator             ")
        print("\t         -----------------------           ")
        print("\t            1.Run Calculator               ")
        print("\t            2. Exit                        ")
        print("\t         -----------------------           ")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            print("\nPresent Operations:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            # User I/P
            num1 = float(input("\tEnter the first number: "))
            num2 = float(input("\tEnter the second number: "))
            operation = input("\tEnter the operation (+, -, *, /): ")
            #logic
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operation"

           #result
            print(f"\n\tResult: {result}")

        elif choice == '2':
            print("Exit the Calculator...")
            break
        else:
            print("Invalid choice. Please choose valid input.")

if __name__ == "__main__":
    calculator()
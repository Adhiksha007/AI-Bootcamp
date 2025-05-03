# addition
def add(a, b):
    return a + b

# Subtract
def subtract(a, b):
    return a - b

# Multiply
def multiply(x, y):
    return x * y

def divide(i, j):
    if j == 0:
        print("Error: Zero Divide")
    else:
        return i / j
    

def Calculator():
    print("Select the Option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter your Choice: ")

        if choice in ['1', '2', '3', '4']:
            x = float(input("Enter first number: "))
            y = float(input("Enter Second Number: "))
            
            if choice == '1':
                print(f"{x} + {y} = {add(x, y)}")
            if choice == '2':
                print(f"{x} - {y} = {subtract(x, y)}")
            if choice == '3':
                print(f"{x} * {y} = {multiply(x, y)}")
            if choice == '4':
                print(f"{x} / {y} = {divide(x, y)}")
                
        next_operation = input("Do you want do another operation(yes/no): ")
        if next_operation.lower() != "yes":
            break
    print("Exiting........")

Calculator()

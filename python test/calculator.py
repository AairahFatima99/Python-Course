def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Selecet one option: ")
print("A for Addition")
print("B for Subtraction")
print("C for Multiplication")
print("D for Division")

num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))

operation = str(input("Pick an operation!"))

if operation == 'A':
    print(f"The result is: {add(num1, num2)}")
elif operation == 'B':
    print(f"The result is: {subtract(num1, num2)}")
elif operation == 'C':
    print(f"The result is: {multiply(num1, num2)}")
elif operation == 'D':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input! Choose a valid option")
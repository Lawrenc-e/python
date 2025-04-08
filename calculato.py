

# Ask the user to enter the numers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operation!"

# Display result
print(f"{num1} {operation} {num2} = {result}")

# Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create
# a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on the operation parameter.
# [operation parameter can have values +, -,* & /.

def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return "Invalid operation"


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))
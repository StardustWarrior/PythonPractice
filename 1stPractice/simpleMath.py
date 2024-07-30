#Calculate the input values with the operator provided
def calc_value(value1, value2, operation='add'):
    if operation.lower() == 'add':
        return f"The addition of {value1} and {value2} is: {int(value1) + int(value2)}"
    elif operation.lower() == "sub":
        return f"The substraction of {value1} and {value2} is: {int(value1) - int(value2)}"
    elif operation.lower() == "mult":
        return f"The addition of {value1} and {value2} is: {int(value1) * int(value2)}"
    elif operation.lower() == "div":
        return f"The addition of {value1} and {value2} is: {int(value1) / int(value2)}"
    else:
        return f"The addition of {value1} and {value2} is: {int(value1) + int(value2)}"

value1 = input("Enter the first value: ")
print(value1)

value2 = input("Enter the second value: ")
print(value2)

operation = input("Add, Sub, Mult or Div: ")
print(operation)

print(calc_value(value1, value2, operation))
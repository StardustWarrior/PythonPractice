number_list = []
sum = 0.0

value = eval(input("Please enter a number (-999 quits): "))

while (value != -999):
    number_list.append(value)
    sum = sum + value
    value = eval(input("Please enter a number (-999 quits): "))

if len(number_list) != 0:
    average = sum / len(number_list)

    print("Using the numbers:")
    for i in range(len(number_list)):
        print (number_list[i], end = " ")

print(f"The average is: {average}")

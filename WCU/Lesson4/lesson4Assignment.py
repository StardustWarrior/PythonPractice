'''
Write a program that reads in a list of numbers from the users and displays the sum and average of this list. 
Your program should enable the users to enter as many numbers as they wish. 
When the users are finished entering numbers, they'll enter the value -1. 
Be sure not to include the -1 in your calculations for the sum and average.
'''
acum = 0
count = 0

while True:
    number = int(input("Enter a number different than -1: "))

    if number != -1:
        acum = acum + number
        count = count + 1
    else:
        break
    
if (count != 0):
    average = acum / count
    
print(f"The total sum of numbers is {acum} and the average is {average}")

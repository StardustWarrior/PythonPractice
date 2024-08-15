'''
Meteorologists use the Saffir-Simpson Scale to classify the strength of hurricanes. 
The intensity is based on the maximum sustained wind speed of a storm as follows:
Category	Wind Speed (mph)
1	74-95
2	96-110
3	111-130
4	131-155
5	156 and higher

Write a Python program that will prompt the user for a wind speed. The program should use this 
wind speed to display a message telling the user the hurricane's intensity based on the table above.
'''

wind_speed = int(input("Enter the wind speed of the hurricane: "))

if wind_speed >= 74 and wind_speed <= 95:
    print("The hurricane is category 1")
elif wind_speed >= 96 and wind_speed <= 110:
    print("The hurricane is category 2")
elif wind_speed >= 111 and wind_speed <= 130:
    print("The hurricane is category 3")
elif wind_speed >= 131 and wind_speed <= 155:
    print("The hurricane is category 4")
elif wind_speed >= 156:
    print("The hurricane is category 5")
else:
    print("Wind speed should be 74 or higher to get the category")

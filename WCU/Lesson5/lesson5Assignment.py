'''
Write a Python program that will print a table of Celsius temperatures and their Fahrenheit 
equivalents between 0 and 100 Celsius in increments of 10 degrees. Your program should include 
a function named convert_to_fahrenheit that takes a Celsius temperature and returns the 
corresponding Fahrenheit temperature.

The formula used to convert a Celsius temperature to a Fahrenheit temperature is this:

Fahrenheit = 9.0/5.0 * Celsius + 32
'''

def convert_to_fahrenheit(celcius_val):
    fahrenheit_val = 9.0/5.0 * float(celcius_val) + 32
    return f"Celcius | {celcius_val} | Fahrenheit | {fahrenheit_val}"

for celcius in range(0, 101, 10):
    print ("\t", convert_to_fahrenheit(celcius))

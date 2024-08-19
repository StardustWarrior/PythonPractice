#Calling a class from another file
from Time2 import Time

myTime1 = Time()
myTime1.set_time(1, 2, 3)
#myTime1.hour = 50
myTime1.print_time()

# Second Time object
myTime2 = Time()
myTime2.set_time(12, 0, 0)

print ("My two time objects are now storing:")
myTime1.print_time()
myTime2.print_time()

#This gives an error since there is a get and set function, you can't access the variable directly
#print (myTime1.__second)

#Not working
myTime1 = Time()
#print (myTime1._Time__second)
#You can use this in your code to get a listing of the documentation string for the class.
print (myTime1.__doc__)
#This attribute will give you the class from which the object was created.
print (myTime1.__class__)
from Time import Time

myTime = Time()

myTime.set_time( 8, 59, 45)

for i in range(20):
    myTime.print_time()
    myTime.tick()
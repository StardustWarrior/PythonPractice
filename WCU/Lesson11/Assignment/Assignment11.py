try:
    counter = 1
    while (counter >= 1):
        number = 2.0 ** counter
        counter = counter + 0.001
except OverflowError:
    print ("Overflow error at value: ", number)
except KeyboardInterrupt:
    print ("Loop interrupted, final value after interruption: ", number)
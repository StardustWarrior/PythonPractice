class Time:
    """ The blueprint for a Time Class object"""
    def __init__ (self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)
#Time Class
class Time:
    """ Blueprint for a Time object"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def tick(self):
        self.__second = self.__second + 1
        if (self.__second == 60):
            self.__second = 0
            self.__minute = self.__minute + 1
            if (self.__minute == 60):
                self.__minute = 0
                self.__hour = self.__hour + 1
                if (self.__hour == 24):
                    self.__hour = 0
    
    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

    #Time Set Functions
    def set_hour(self, hour):
        self.__hour = hour

    def set_minute(self, minute):
        self.__second = second

    def set_second(self, second):
        self.__second = second

    #Time Get Functions
    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second
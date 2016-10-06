import time

class ShamsiFormatter():
    __reminders1 = [1, 5, 9, 13, 17, 22, 26, 30]
    __reminders2 = [1, 5, 9, 13, 18, 22, 26, 30]

    __current_milli_time = lambda x: int(round(time.time()))



    def __init__(self):
        self.__cons(self.__current_milli_time()-6739200)

    def __cons(self,second):
        self.__seconds = second
        self.__days = self.__calcDays(self.__seconds)
        self.__year,self.__remindDays = self.__calcYears(self.__days)
        self.__mounth = self.__calcMounth()

    def __calcDays(self,seconds):
        dayLong = 24*3600
        return int(seconds/dayLong)

    def __calcYears(self,days):
        year = 1349
        NormalYearLong = 365
        KabiseYearLong = 366
        while ((days > 366 and self.__IsLeapYear(year)) or (days > 365 and not self.__IsLeapYear(year))):
            if (self.__IsLeapYear(year)):
                days = days - KabiseYearLong
            else:
                days = days - NormalYearLong
            year += 1
        return year,days

    def __calcMounth(self):
        mounthCount = 1
        remind = self.__remindDays
        while ((remind>31 and mounthCount <=6 ) or (remind>30 and mounthCount <=11 and mounthCount > 6)):
            mounthLong = self.__getMounthLong(mounthCount,self.__year)
            remind -= mounthLong
            mounthCount += 1
        self.__remindDays = remind
        return mounthCount


    def __getMounthLong(self,mounth,year):
        if mounth == 12:
            if self.__IsLeapYear(year):
                return 30
            else:
                return 29
        elif mounth <= 6:
            return 31
        else:
            return 30

    def __IsLeapYear(self,year):
        remind = year % 33
        if (year >= 1244 and year <= 1342 and remind in self.__reminders1):
            return True
        elif (year >= 1343 and year <= 1472 and remind in self.__reminders2):
            return True
        else:
            return False

    def getDay(self):
        return self.__remindDays

    def getYear(self):
        return self.__year

    def getMounth(self):
        return self.__mounth

    def getWeekDay(self):
        week = self.__days % 7
        return  {
            0:'جمعه',
            1:'شنبه',
            2:'یکشنبه',
            3:'دوشنبه',
            4:'سه شنبه',
            5:'چهارشنبه',
            6:'پنجشنبه',
        }[week]

    def getMountString(self):
        return {
            1:'فروردین',
            2:'اردیبهشت',
            3:'خرداد',
            4:'تیر',
            5:'مرداد',
            6:'شهریور',
            7:'مهر',
            8:'آبان',
            9:'آذر',
            10:'دی',
            11:'بهمن',
            12:'اسغند',
        }[self.__mounth]





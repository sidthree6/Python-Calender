class Calender:
    def __init__(self, year, month):
        self.months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December")
        self.monthDays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        self.days = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
        self.month = month
        self.year = year

    def printCalenderMonth(self):
        i = 1
        step = 0

        while i <= self.returnMonthDay(self.month-1, self.year):
            # print(self.findStartDayOfMonth(self.month))
            if step > self.findStartDayOfMonth(self.month):
                if i < 10:
                    print("   {}".format(i), end=" ")
                else:
                    print("  {}".format(i), end=" ")
                if step % 7 == 0:
                    print("\n")
                i += 1
            else:
                print("    ", end=" ")
                if step % 7 == 0:
                    print("\n")

            step += 1

    def printMonth(self):
        return self.months[self.month - 1]

    def printWeekDays(self):
        return self.days

    def isLeapYear(self, year):
        if year % 4 == 0 and not year % 100 == 0:
            return True
        elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 == 0:
            return False
        else:
            return False

    def dayChecker(self, day):
        return day % 7

    def findFirstDayOfYear(self):
        start = 1900
        curr_day = 0

        for i in range(start, self.year+1):
            if self.isLeapYear(i-1):
                curr_day += 2
            else:
                curr_day += 1

        return self.dayChecker(curr_day)

    def returnMonthDay(self, month, year):
        if self.isLeapYear(year) and month == 1:
            return 29
        return self.monthDays[month]

    def findStartDayOfMonth(self, month):
        firstDay = self.findFirstDayOfYear()

        for i in range(0, month-1):
            if i is not month-1:
                firstDay += self.returnMonthDay(i, self.year)

        return self.dayChecker(firstDay)

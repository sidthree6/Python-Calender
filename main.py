from custom_calender import Calender

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = Calender(year, month)

print("{}, {}".format(cal.printMonth(), year))

for i in cal.printWeekDays():
    print("{}".format(i), end="  ")


cal.printCalenderMonth()



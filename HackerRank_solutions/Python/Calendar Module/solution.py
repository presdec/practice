# url : https://www.hackerrank.com/challenges/calendar-module/problem


import calendar


s = input()
a = s.split(sep=" ")
day = calendar.weekday(int(a[2]), int(a[0]), int(a[1]))
text = (calendar.day_name[day])
formated = text.upper()
print(formated)

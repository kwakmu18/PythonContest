import calendar
weekdays=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
m,d,y=map(int, input().split())
print(weekdays[calendar.weekday(y,m,d)])
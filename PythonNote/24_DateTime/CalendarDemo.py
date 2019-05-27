import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
current = c.formatmonth(2019, 5, 0, 0)
print(current)

c2 = calendar.HTMLCalendar(calendar.SUNDAY)
current2 = c2.formatmonth(2019, 5)
print(current2)

from datetime import date
from datetime import time
from datetime import datetime, timedelta


today = date.today()

print("오늘 날짜: ", today)

print("년, 월, 일: ", today.year, today.month, today.day)

print("요일 인덱스: ", today.weekday()) # 0(월) ~ 6(일)

print("날짜 전체: ", datetime.now())
print("시간 전체: ", datetime.time(datetime.now()))


print("오늘: " + str(datetime.now()))

one_day = timedelta(days=1) # timedelta == TimeSpan

yesterday = today - one_day

print("어제: " + str(yesterday))


birthday = input("생일: (dd/mm/yyyy)? ")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print("생일: " + str(birthday_date)) # yyyy-MM-dd

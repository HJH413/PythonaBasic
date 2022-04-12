"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

from datetime import date

today = date.today()
print("오늘은 ?", today)
print("오늘은 ?", today.year)
print("오늘은 ?", today.month)
print("오늘은 ?", today.day)

from datetime import datetime, timedelta
today = datetime.today()
print("오늘은 ?", today.hour)
print("-"*50)
print("today is", today + timedelta(days=10))
print("today is", today + timedelta(days=-10))
#오늘 날짜에서 3개월 후
print(today+timedelta())

from dateutil.relativedelta import relativedelta
print(today + relativedelta(months=3))
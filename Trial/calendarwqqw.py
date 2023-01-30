import calendar
from datetime import datetime,date,timedelta
CurrentDate = date.today()
currentMonthCount = calendar.monthrange(date.today().year,date.today().month)[1]
NumberOfDaysNotInMonth = 42 - currentMonthCount
PreviousMonthCount = date.today().replace(day=1) - timedelta(days=1)
PreviousMonthCount = PreviousMonthCount.day
print(CurrentDate)
print(currentMonthCount)
print(PreviousMonthCount)

from datetime import date

import datetime
datetime.datetime.today()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)




dayOfWeek = ["Thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "chủ nhật"]

# print(dayOfWeek[today])

def getDayOfWeek():
    today = datetime.datetime.today().weekday()
    return dayOfWeek[today]



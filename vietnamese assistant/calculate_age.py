from datetime import date


def calculateAge(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# born = date()



          #year month day 
dob = date(2020, 11, 14) 
# print(calculateAge(dob))

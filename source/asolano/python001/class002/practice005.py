def days_in_month(month):
    days = 0
    if month.upper() == "JANUARY":
        days = 31
    elif month.upper() == "FEBRUARY":
        days = 28
    elif month.upper() == "MARCH":
        days = 31
    elif month.upper() == "APRIL":
        days = 30
    if month.upper() == "MAY":
        days = 31
    elif month.upper() == "JUNE":
        days = 30
    elif month.upper() == "JULY":
        days = 31
    elif month.upper() == "AUGUST":
        days = 31
    if month.upper() == "SEPTEMBER":
        days = 30
    elif month.upper() == "OCTOBER":
        days = 31
    elif month.upper() == "NOVEMBER":
        days = 30
    elif month.upper() == "DECEMBER":
        days = 31
    else:
        days = "NONE"
    return (days)

month = raw_input("enter month: ")
result = days_in_month(month)
print (result)
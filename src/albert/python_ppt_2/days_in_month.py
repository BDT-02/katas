def days_in_month(m):

    switch = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    return switch.get(m.capitalize(), None)


month = str(raw_input("Enter the month: "))

days = days_in_month(month)

if days:
    print(month + " has " + str(days_in_month(month)) + " days")
else:
    print(month + " doesn't exists!!")

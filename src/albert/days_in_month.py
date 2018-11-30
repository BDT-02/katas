def days_in_month(month):

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

    return switch.get(month.capitalize(), None)


month = input("Enter the month: ")

days = days_in_month(month)

if days:
    print(month, " has ", days_in_month(month), " days")
else:
    print(month, " doesn't exists!!")

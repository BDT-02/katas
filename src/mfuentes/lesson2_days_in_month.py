#Write a function days_in_month which takes the name of a month, and returns the number of days
# in the month. Ignore leap years:
# days_in_month("February") == 28 	days_in_month("December") == 31
# If the function is given invalid arguments, it should return None.
def days_in_month(month):
    list = ['January', 'March','May','July', 'August', 'October', 'December']
    list1 = ['April','June','September','November']

    if month in list:
        print(31)
    elif month in list1:
        print(30)
    elif month == 'February':
        print(28)
    else:
        print('None')

month = str(input("Enter a month: "))

days_in_month(month)

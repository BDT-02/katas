def msg(age):
    if age <= 12:
        print "\nYou are a child, when the age is lower than 12"
    elif age >= 13 and age <= 17:
        print "\nYour are teenager, when the age is between 13 and 17"
    elif age >= 18 and age <= 29:
        print "\nYou are young, when the age is between 18 and 29"
    else:
        print "\nYou are adult, when the age is greater than 30"

#Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:

def replace(s, old, new):
    wds = s.split(old)
    glue = new
    new = glue.join(wds)
    print(new)


s = str(input("Enter a string: "))
old = str(input("Enter an old : "))
new = str(input("Enter a new value: "))
replace(s, old, new)
#replace("Mississippi", "i", "I")
#replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am")




def replace(s, old, new):
    num = s.count(old)
    # returns the same string if "old" isn't found
    if num < 1:
        return s

    str_list = s.split(old)
    result = ''
    for txt in str_list:
        if num > 0:
            result += txt + new
            num -= 1
        else:
            result += txt

    return result


song = "I love spom! Spom is my favorite food.Spom, spom, yum!"
print replace(song, "om", "am")
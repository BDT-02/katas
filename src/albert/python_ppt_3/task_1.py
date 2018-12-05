text = "any text in http://local.com is not allowed"
index = text.find("http://")
if index >= 0:
    index2 = text.find(" ", index)
    print(text[index:index2])
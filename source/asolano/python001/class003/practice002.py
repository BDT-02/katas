def replace(stringg,old,new):
    lenSubString = len(old)
    lenString = len(stringg)
    stringg.find(old)

    lenSubString = len(old)
    lenString = len(stringg)
    find_space = stringg.find(old)
    while (find_space != -1):
        sub_url = stringg[0:find_space] + new + stringg[find_space+lenSubString:lenString]
        stringg = sub_url
        find_space = stringg.find(old)
    return stringg

stringg = "I love spom, spom is my favorite spom"
old = "om"
new = "an"
print("source string: ",stringg)
result = replace(stringg,old,new)
print("target source: ",result)
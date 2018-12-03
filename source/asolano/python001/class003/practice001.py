def review_space(url):
    len1 = len(url)
    find_space = url.find(" ")
    while (find_space != -1):
        sub_url = url[0:find_space] + url[find_space+1:len1]
        url = sub_url
        find_space = url.find(" ")
    return url

url = raw_input("enter url: ")
result = review_space(url)
print(result)
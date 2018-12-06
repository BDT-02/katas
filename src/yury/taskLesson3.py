def get_url(text):
    urls = []
    size = len(text)
    start = text.find("http://")
    while start != -1:
        sub_text = text[start: size]
        end = sub_text.find(" ")
        urls.append(sub_text[0: end])
        text = text[end + start: size]
        start = text.find("http://")
    return urls


def replace_text(s, old, new):
    return s.replace(old, new)


def fill_list():
    list = []
    value = input()
    list.append(value)
    return list


def show_list(list):
    print (list)


def count_repetitions_alphabet(text):
    dict = {}
    text = text.replace(" ", "")
    for index in text:
        if index in dict.keys():
            dict[index] += 1
        else:
            dict[index] = 1
    print dict
    return dict


def read_phrase(data):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter_dict = {}
    for c in alphabet:
        num = data.count(c)
        if num > 0:
            counter_dict[c] = num

    return counter_dict


phrase = raw_input("Enter the phrase: ")
result = read_phrase(phrase)

for key, value in result.items():
    print str(key) + ": " + str(value)

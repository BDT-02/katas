def count_element(strings):
    sortedS = ''.join(sorted(strings.lower()))
    print(sortedS)
    count = 0
    len1 = len(sortedS)
    while (count <= len1):
        repeateble = 1
        letter = sortedS[count]
        if (sortedS[count+1] != " "):
            while (sortedS[count] == sortedS[count+1]):
                repeateble += 1
                count += 1
        print(letter, "  ",repeateble)
        count += 1

strings = raw_input("insert string: ")
count_element(strings)
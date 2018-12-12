def revrot(number, sz):
    result = ""
    while len(number) >= sz > 0:
        aux = 0
        part_str = number[0:sz]
        for num in part_str:
            aux += int(num)
        result += part_str[::-1] if aux % 2 == 0 else part_str[1:] + part_str[:1]
        number = number[sz:]
    return result


def testing(actual, expected):
    assert actual == expected


testing(revrot("1234", 0), "")
testing(revrot("", 0), "")
testing(revrot("1234", 5), "")
s = "733049910872815764"
testing(revrot(s, 5), "330479108928157")

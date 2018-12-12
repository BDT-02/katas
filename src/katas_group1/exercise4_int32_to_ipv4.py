def int32_to_ip(int32):
    binario = "{0:b}".format(int32)
    lista = []
    while len(binario) > 0:
        lista.append(str(int(binario[-8:], 2)))
        binario = binario[:-8]

    while len(lista) < 4:
        lista.append('0')

    lista.reverse()
    return ".".join(lista)

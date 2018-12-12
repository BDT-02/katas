def get_middle(word):
    if(len(word) % 2 == 0):
        print "" + word[(int(len(word) / 2) -1)] + word[(int(len(word) / 2))]
    else:
        print word[(int(len(word)/2))]

print get_middle('Bolivia')
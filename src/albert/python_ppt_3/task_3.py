def function1():
    num = int(raw_input("How many items you want to insert: "))
    array = []
    for i in range(1, num + 1):
        array.append(raw_input("Item {}: ".format(i)))

    return array


def function2(args):
    print args


arg = function1()
function2(arg)

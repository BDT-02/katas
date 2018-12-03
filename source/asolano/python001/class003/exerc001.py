global_val = 2

def h2():
    global global_val
    global_val = global_val + 1
    print (global_val)

h2()
print(global_val)
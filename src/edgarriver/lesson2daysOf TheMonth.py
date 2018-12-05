def mont(m):

    if(m >= 3 and m <= 12 or m == 1):
        if(m<=7):
            if(m % 2==0):
                print("el mes "+str(m)+" tiene 30 dias")
            else:
                print("el mes "+str(m)+" tiene 31 dias")
        else:
            if(m % 2==0):
                print("el mes "+str(m)+" tiene 31 dias")
            else:
                print("el mes "+str(m)+" tiene 30 dias")
    else:
        print("el mes tiene 28 dias ")

mont(int(input("ingresa el numero del mes(1 January, 2 February, 3 March, 4 April, 5 May, 6 June, 7 July, 8 August, 9 September, 10 October, 11 November, 12 Dicember )\n")))
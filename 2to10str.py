while True:
    arv = input("Sisesta kahendsüsteemis olev arv: ")
    uusArv = 0
    index = len(arv) - 1


    for i in arv:

        i = int(i)

        uusArv += i*(2**index)
        index -= 1

    print(uusArv)
    print()

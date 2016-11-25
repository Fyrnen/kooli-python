def encrypt(mode):
    if mode == 'y':
        fs = open('text_sis.txt', 'r')
        tekst = fs.read().lower()
        fs.close()
        
    else:
        tekst = input("Kirjuta siia midagi: ").lower()
        
    enTekst = ""
    index = 0
    
    for i in tekst:
        if 97 <= ord(i) <= 122:
            index = ord(i) + 8

            if index > 122:
                index -= 26

            else:
                pass

            enTekst += chr(index)
            
        else:
            enTekst += i

    if mode == 'y':
        fv = open('text_val.txt', 'w')
        fv.write(enTekst)
        fv.close()

    else:
        print(enTekst)

def decrypt(mode):
    if mode == 'y':
        fs = open('text_sis.txt', 'r')
        enTekst = fs.read().lower()
        fs.close()
        
    else:
        enTekst = input("Kirjuta siia midagi: ").lower()

    tekst = ""
    index = 0

    for i in enTekst:
        if 97 <= ord(i) <= 122:
            index = ord(i) - 8

            if index < 97:
                index += 26

            else:
                pass

            tekst += chr(index)
            
        else:
            tekst += i

    if mode == 'y':
        fv = open('text_val.txt', 'w')
        fv.write(tekst)
        fv.close()

    else:
        print(tekst)

x = 0

while x == 0:
    anw = input("Kirjuta 1, kui soovid krüpteerida ja 2, kui soovid dekrüpteerida: ")
    
    if anw ==  '1':
        mode = input("Kas soovid krüpteerida tekstifaili? (y/n) ")
        print()
        encrypt(mode)

    elif anw == '2':
        mode = input("Kas soovid dekrüpteerida tekstifaili? (y/n) ")
        print()
        decrypt(mode)
        
    elif anw == 'close':
        anw = input("Kas soovid programmi välja lülitada? (y/n) ")
        print()

        if anw == 'y':
            x = 1

        else:
            pass
    else:
        pass

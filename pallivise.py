
tulemused = []
pauliKoht = 1
pauliKohtJag = 1
pauliVise = 0
lasteArv = 0
jag = 0
e = 0

while e == 0:
    try:
        pauliVise = float(input('Kui kaugele viskas Paul palli? '))
        
        if pauliVise <= 0:
            print('Palun sisesta adekvaatsed väärtused \n')
            continue
        else:
            e = 1

        lasteArv = int(input('Kui palju lapsi viskas peale Pauli palli? '))
        
        if lasteArv < 0:
            print('Palun sisesta adekvaatsed väärtused \n')
            continue
        else:
            e = 1
                
    except ValueError:
        print('Palun sisesta adekvaatsed väärtused \n')
        e = 0

for i in range(lasteArv):
    
    try:
        tul = float(input('Kui kaugele viskas ' + str(i+1) + '. laps? '))
        
    except ValueError:
        print('Palun sisesta adekvaatsed väärtused \n')

    if tul <= 0:
        print('Palun sisesta adekvaatsed väärtused \n')
                                     
    else:
        tulemused.append(tul)

for i in tulemused:
    
    if i > pauliVise:
        pauliKoht += 1

        if jag == 1:
            pauliKohtJag += 1

    elif i < pauliVise:
        pass

    elif i == pauliVise:
        pauliKohtJag = pauliKoht + 1
        jag = 1

if jag == 1:
    print('Paul jagab ' + str(pauliKoht) + '. kuni ' + str(pauliKohtJag) + '. kohta.')

else:
    print('Paul saavutas ' + str(pauliKoht) + '. koha.')
input()


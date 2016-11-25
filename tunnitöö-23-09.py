'''
---Ülesanne 1---

a = int(input('Sisesta arv: '))

if (a % 2 == 0):
    print('Sisestatud arv on paaris.')
else:
    print('Sisestarud arv on paaritu.')
print('')

---Ülesanne 2---

a = int(input('Sisesta esimene arv: '))
b = int(input('Sisesta teine arv: '))

if (a > b):
    if (a % b == 0):
        print (str(a) + ' jagub arvuga ' +  str(b) + '.')
    else:
        print (str(a) + ' ei jagu arvuga ' +  str(b) + '.')
        
elif (b > a):
    if (b % a == 0):
        print (str(b) + ' jagub arvuga ' +  str(a) + '.')
    else:
        print (str(b) + ' ei jagu arvuga ' +  str(a) + '.')

elif (a == b):
    print('Mõlemad arvud jaguvad teineteisega')

---Ülesanne 3---

a = input('Kui pikk on Juhani esimene kaigas? ')
b = input('Kui pikk on Juhani teine kaigas? ')
c = input('Kui pikk on Juhani kolmas kaigas? ')

if ((a + b) > c and c > a and c > b):
    print('Kolmnurka saab moodustada')
else:
    print('Kolmnurka ei saa moodustada')

if ((a + c) > b and b > a and b > c):
    print('Kolmnurka saab moodustada')
else:
    print('Kolmnurka ei saa moodustada')

if ((c + b) > a and a > c and a > b):
    print('Kolmnurka saab moodustada')
else:
    print('Kolmnurka ei saa moodustada')

---Ülesanne 4---
'''
import math

a = int(input('Sisesta ruutvõrrandi kordaja a: '))
b = int(input('Sisesta ruutvõrrandi kordaja b: '))
c = int(input('Sisesta ruutvõrrandi kordaja c: '))

if(a == 0):
    print('Ruutvõrrandit ei teki')
else:
    try:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))
        
    except ValueError:
        print('Reaalarvulised lahendid puuduvad')




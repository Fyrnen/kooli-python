import sys
import decimal

def pTul(a):

    if a <= 135:

        b = a

    elif a > 135:

        b = a - (0.21 * (a - 135))

    return b

def aTul(a):

    if a <= 100:

        b = a

    elif a > 100 and a <= 400:

        b = a - (0.15 * (a - 100))

    elif a > 400 and a <= 1000:

        b = a - (0.26 * (a - 100))

    elif a > 1000:

        b = a - (0.33 * (a - 100))

    return b

x = float(input('Sisesta oma brutopalk: '))

while x <= 0:
    x = float(input('Sisesta oma päris brutopalk: '))

pPalk = decimal.Decimal(str(pTul(x)))
aPalk = decimal.Decimal(str(aTul(x)))

if pPalk > aPalk:

    print('Sinule on soodsam propotsionaalne tulumaks.')
    print('Sel juhul on netopalk ' + str(pPalk) + ' eurot.')
    print('Astmelise tulumaksuga võrreldes võidad ' + str(pPalk - aPalk) + ' eurot.')

elif aPalk > pPalk:

    print('Sinule on soodsam astmeline tulumaks.')
    print('Sel juhul on netopalk ' + str(aPalk) + ' eurot.')
    print('Propotsionaalse tulumaksuga võrreldes võidad ' + str(aPalk - pPalk) + ' eurot.')

elif aPalk == pPalk:

    print('Sinu palga puhul on astmeline ja propotsionaalne tulumaks võrdsed.')

input()

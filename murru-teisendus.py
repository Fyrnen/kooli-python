x = float(input('Sisesta kümnendmurd: '))

y = '0.'

while x != 0:

    x += x
    
    if x >= 1:

        y += '1'
        x -= 1

    elif x < 1:

        y += '0'

print(y)

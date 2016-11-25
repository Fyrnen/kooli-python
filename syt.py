c = 1
cont = 'y'

def syt(x, y):

	while y > 0:
		
		r = x % y
		x = y
		y = r

	return x


while c == 1:

	a = int(input('Sisesta suurem arv: '))
	b = int(input('Sisesta väiksem arv: '))

	print(syt(a, b))

	while cont == 'y':

		cont = input('Kas tahad uuesti leida suurimat ühistegurit? (y/n) ')

		if cont == 'y':
			break

		elif cont == 'n':
			c = 0
			break

		else:
			cont = 'y'
			print('Palun sisesta kas "y" või "n". ')

input()
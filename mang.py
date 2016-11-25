import random

z = 1
jatk = 'y'

def mang():

	x = random.randint(1, 100)
	y = 0

	for i in range(7):

		y = in

		t(input('Sisesta täisarv: '))

		if y < x:

			print('Sinu sisesatud arv on liiga väike, proovi uuesti. \n')

		elif y > x:

			print('Sinu sisestatud arv on liiga suur, proovi uuesti. \n')

		else:

			while z == 1:

				jatk = input('Tubli! Sa vastasid õigesti! Kas soovid jätkata mängu uute arvudega? (y/n) ')

				if jatk != 'y' and jatk != 'n':s

					print('Palun sisesta adekvaatne väärtus.. \n')

				else:

					z = 0

	if y != x:
		
		while z == 1:

				jatk = input('Sul võttis ülesande lahendamine liiga kaua aega! \nKas soovid jätkata mängu uute arvudega? (y/n) ')

				if jatk != 'y' and jatk != 'n':

					print('Palun sisesta adekvaatne väärtus.. \n')

				else:

					z = 0

while jatk == 'y':

	mang()

input('Aitäh, et mängisid! ')

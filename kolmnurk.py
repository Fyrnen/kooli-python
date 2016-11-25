import math

a = input("Sisesta täisnurkse kolmnurga esimene kaatet: ")
b = input("Sisesta täisnurkse kolmurga teine kaatet: ")

a = int(a)
b = int(b)

c = math.sqrt(a**2 + b**2)

ymber = a + b + c
ymber = str(ymber)

pind = (a*b)/2
pind = str(pind)

print("Kolmnurga ümbermõõt on " + ymber + " ja pindala on " + pind + ".")
input()

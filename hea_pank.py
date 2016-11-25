import sys

n = float(input("Sisestage oma kontole kantav raha: "))
k = float(input("Sisestage oma kontole igas kuus lisatav summa: "))
p = float(input("Sisestage aastane intressimäär: "))
l = float(input("Mitu eurot tahate hoiusele koguda? "))

if n >= l:
    print("Teil on juba soovitud raha olemas, milles probleem?")
    input()
    sys.exit()

pk = p/12
i = 0

x = n + n*(p/100)

while x < l:

    i += 1
    x += k
    x += x*(pk/100)

a = i // 12
b = i % 12

print("Teie soovitud raha kogumiseks kulub " + str(a) + " aastat ja " + str(b) + " kuud.")
input()

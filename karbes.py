
s1 = int(input("Sisesta jalgratturi kaugus kodust: "))
v1 = int(input("Sisesta jalgratturi kiirus: "))
v2 = int(input("Sisesta kärbse kiirus: "))

t = s1/v1
s2 = str(v2*t)

print("Kärbes läbis " + s2 + " km.")
input()

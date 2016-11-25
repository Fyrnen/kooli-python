import math

print('   Arv     Ruut  Kuup  Ruutjuur')

for i in range(20):
    print(repr(i).rjust(6), repr(i*i).rjust(6), repr(i*i*i).rjust(6), repr(round(math.sqrt(i), 2)).rjust(6))

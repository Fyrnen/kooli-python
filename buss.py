t1 = input('Sisesta bussi väljumisaeg tundides ja minutites (hh:mm): ')
t2 = input('Sisesta bussi saabumisaeg tundides ja minutites (hh:mm): ')

h1, m1 = t1.split(':')
h2, m2 = t2.split(':')

h1 = int(h1)
h2 = int(h2)
m1 = int(m1)
m2 = int(m2)

t1 = h1 + (m1 / 60)
t2 = h2 + (m2 / 60)

dt = t2 - t1

h = int(dt)
m = dt - h

m = round(m * 60)

print('Buss sõidab ' + str(h) + ' h ja ' + str(m) + ' m.')
input()

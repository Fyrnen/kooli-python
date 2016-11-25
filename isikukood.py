import time

kuudeList = {'jaanuar': 1, 'veebruar': 2, 'marts': 3, 'aprill': 4, 'mai': 5, 'juuni': 6, 'juuli': 7, 'august': 8, 'september':9, 'oktoober': 10, 'november': 11, 'detsember': 12}

kood = str(input("Mis on su isikukood? "))

if (int(kood[0]) % 2) == 1:
    sugu = "mees"
else:
    sugu = "naine"

synniPaev = int(kood[5])*10+int(kood[6])

for kuuNimi, kuuNumber in kuudeList.items():
    if kuuNumber == (int(kood[3])*10+int(kood[4])):
        kuu = kuuNimi

aasta = ((int(kood[0])+1)//2)*100+1700 + int(kood[1])*10+int(kood[2])

print ("Sa oled sündinud %d. %s %d ja sa oled %s" %(synniPaev, kuu, aasta, sugu))
		

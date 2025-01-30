import pywhatkit
import datetime
import time

hedef_numara = "+994xxxxxxxxx"
saat = "14:50"
mesaj = "Günaydınnnnnnn"
gonderilecek_saat = int(saat.split(":")[0])
gonderilecek_dakika = int(saat.split(":")[1])

zaman = datetime.datetime.now().replace(hour=gonderilecek_saat,minute=gonderilecek_dakika,second=0,microsecond=0)

if zaman<datetime.datetime.now():
yarin = datetime.date.today() + datetime.timedelta(days=1)
zaman = datetime.datetime.combine(yarin,datetime.time(gonderilecek_saat,gonderilecek_dakika))

dk_sonra = zaman+datetime.timedelta(minutes=1)

while True:
now = datetime.datetime.now()
if now.hour== gonderilecek_saat and now.minute==gonderilecek_dakika :
pywhatkit.sendwhatmsg(hedef_numara,mesaj,gonderilecek_saat,gonderilecek_dakika+1)
print("Gönderildi")

yarin = datetime.date.today() + datetime.timedelta(days=1)
zaman = datetime.datetime.combine(yarin,datetime.time(gonderilecek_saat,gonderilecek_dakika))
dk_sonra = zaman+datetime.timedelta(minutes=1)

time.sleep(60)
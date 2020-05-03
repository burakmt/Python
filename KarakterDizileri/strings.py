name = 'Burak'
surname = 'Ekici'
age = 24

print(name + ' ' + surname + ' \nYaş: ' + str(age))

#KARAKTER SAYISI
length = len(name)
#SON KARAKTERİ ALMA
lastChar = name[-1]
#İKİ DEĞER ARASI KARAKTER SEÇME
choiseChar = name[1:3]
#BAŞLANGIÇ DEĞERİNDEN SONRAKİ KARAKTERLERİ SEÇME
startCharIndex = name[1:]
#KARAKTERLERİ ARİTMETİK ŞEKİLDE SEÇME (x,y,z) x--> Başlangıç Değeri y--> Bitiş Değeri z--> Kaç karakter atlayacağı ÖRN: z=2 ise bir karakter alır bir karakter atlar
arChoiseChar = name[0:4:2]
print(arChoiseChar)
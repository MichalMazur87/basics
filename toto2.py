import random

ileliczb = int(input("Ile liczb chcesz odgadnąć?"))
#print (ileliczb)
maksliczba = int(input("Jaka jest maksymalna losowana liczba?"))
#print (maksliczba)

#losujemy liczby
liczby=[]
i=0
while i < ileliczb:
    liczba=random.randint(1,maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i+=1

#pobieramy typy od użytkownika
print ("Wytypuj ",ileliczb," z ",maksliczba," liczb: ")
print("Wytypuj %d z %d liczb: " % (ileliczb,maksliczba)) #to samo z innym zapisem, %s string, %d dziesiętna, %f float
typy=set()
i=0
while i < ileliczb:
    typ = input("podaj liczbę %s: " % (i+1))
    if typ not in typy:
        typy.add(typ)
        i+=1

print("Wylosowane liczby: ", typy)
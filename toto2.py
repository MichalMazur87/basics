import random

ileliczb = int(input("Ile liczb chcesz odgadnąć?"))
#print (ileliczb)
maksliczba = int(input("Jaka jest maksymalna losowana liczba?"))
#print (maksliczba)
#print ("Wytypuj ",ileliczb," z ",maksliczba," liczb: ")
print("Wytypuj %d z %d liczb: " % (ileliczb,maksliczba)) #to samo z innym zapisem, %s string, %d dziesiętna, %f float

i=0
wylosowane=[]
while i < ileliczb:
    liczba = random.randint(1,maksliczba)
    print(liczba)
    if wylosowane.count(liczba)==0:
        wylosowane.append(liczba)
        i+=1




print("Wylosowane liczby: ", wylosowane)
    
import random

ileliczb = input("Ile liczb chcesz odgadnąć?")
ileliczb = int(ileliczb)
print (ileliczb)
maksliczba = int(input("Jaka jest maksymalna losowana liczba?"))
print (maksliczba)
#print ("Wytypuj ",ileliczb," z ",maksliczba," liczb: ")
print("Wytypuj %d z %d liczb: " % (ileliczb,maksliczba)) #to samo z innym zapisem, %s string, %d dziesiętna, %f float
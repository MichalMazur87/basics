import random



try:
    ileliczb = int(input("Ile liczb chcesz odgadnąć?"))
    #print (ileliczb)
    maksliczba = int(input("Jaka jest maksymalna losowana liczba?"))
    #print (maksliczba)
    if ileliczb > maksliczba:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błądne dane!")
    exit()


#losujemy liczby
liczby=[]
i=0
while i < ileliczb:
    liczba=random.randint(1,maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i+=1

for n in range(3):
    #pobieramy typy od użytkownika
    print("Próba %s z 3" % (n+1))
    print("Wytypuj %d z %d liczb: " % (ileliczb,maksliczba)) #to samo z innym zapisem, %s string, %d dziesiętna, %f float
    typy=set()
    i=0
    while i < ileliczb:
        try:
            typ = int(input("podaj liczbę %s: " % (i+1)))
        except ValueError:
            print("Błędne dane:")
            continue

        if typ not in typy and 0<typ<=maksliczba:
          typy.add(typ)
          i+=1
        
        elif typ in typy:
            print("Zdublowana liczba")

        else:
            print("Liczba poza zakresem")

    
    #prezentacja wyników
    trafione = set(liczby) & typy
    if trafione:
        print("Ilość trafień: %s z %s" % ((len(trafione)),ileliczb))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")
    n+=1
    print("\n", "########################################" * 10, "\n")
uppskattade_minuter = int(input("Hur många minuter uppskattar du att du ringer per månad? "))

if uppskattade_minuter < 33:
    print("Du bör välja abonnemanget KONTANT")
    print("Du ringer inte så mycket")

elif uppskattade_minuter > 33 and uppskattade_minuter < 66:
    print("Du bör välja abonnemanget Normal")
    print("Du ringer lika mycket som dom flesta")

else:
    print("Du bör välja abonnemanget PLUS")
    print("Du ringer väldigt mycket")


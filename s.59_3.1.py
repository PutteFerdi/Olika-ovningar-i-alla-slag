svar = input("Hur många minuter uppskattar du att du ringer per månad? ")

if svar < "33":
    print("Du bör välja abonnemanget KONTANT")
    print("Du ringer inte så mycket")

if svar == "33":
    print("Du bör välja abonnemanget KONTANT")
    print("Du ringer inte så mycket")

if svar > "33" < "67":
    print("Du bör välja abonnemanget Normal")
    print("Du ringer lika mycket som dom flesta")

if svar > "66":
    print("Du bör välja abonnemanget PLUS")
    print("Du ringer väldigt mycket")


svar = input("Vilken timme är det? ")

if svar < '12':
    sängen = input("Har du klivit upp ur sängen än? ")
    if sängen == "ja":
        print("Bra, du har faktiskt tagit tag i ditt liv")
    elif sängen == 'nej': 
            print("kliv upp för fan!")

if svar > '12':
    print("Hämta bärsen det är dags!")

if svar == "12":
    print("Gör något kul")

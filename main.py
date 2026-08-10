
def hlavni_menu():

    print("Správce úkolů - Hlavní menu")

    ukoly = []
    ukoly.append("1. Přidat nový úkol")
    ukoly.append("2. Zobrazit všechny úkoly")
    ukoly.append("3. Odstranit úkol")
    ukoly.append("4. Konec programu")

    for typUkolu in ukoly:
        print(typUkolu)

    cislo_Ukolu = input("Vyberte možnost (1-4) : ")

    return(cislo_Ukolu)


def pridatUkol(seznamUkolu):
    nazevUkolu = input("Zadejte nazev ukolu : ")
    popisUkolu = input("Zadejte popis ukolu : ")

    nazevAPopisUkolu = []
    nazevAPopisUkolu.append(nazevUkolu)
    nazevAPopisUkolu.append(popisUkolu)

    seznamUkolu.append(nazevAPopisUkolu)

    return(seznamUkolu)


def zobrazit_ukoly(seznamUkolu):

    print("Seznam úkolů:")
    i1 = 0

    for nazevAPopisUkolu in seznamUkolu:
        i1 = i1 + 1
        nazevUkolu = nazevAPopisUkolu[0]
        popisUkolu = nazevAPopisUkolu[1]

        text = str(i1) + ". " + nazevUkolu + " - " + popisUkolu

        print(text)

    

seznamUkolu = []
cislo_Ukolu = hlavni_menu()


if cislo_Ukolu == "1":
    seznamUkolu = pridatUkol(seznamUkolu)


zobrazit_ukoly(seznamUkolu)


#if cislo_Ukolu == "2":
#    zobrazit_ukoly(seznamUkolu)








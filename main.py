def hlavni_menu():
    print("Správce úkolů - Hlavní menu")

    ukoly = []
    ukoly.append("1. Přidat nový úkol")
    ukoly.append("2. Zobrazit všechny úkoly")
    ukoly.append("3. Odstranit úkol")
    ukoly.append("4. Konec programu")

    for typUkolu in ukoly:
        print(typUkolu)


def pridatUkol(seznamUkolu):
    nazevUkolu = input("Zadejte nazev ukolu : ")
    popisUkolu = input("Zadejte popis ukolu : ")

    nazevAPopisUkolu = {
          "nazevUkolu": nazevUkolu,
          "popisUkolu": popisUkolu
    }

    seznamUkolu.append(nazevAPopisUkolu)

    return (seznamUkolu)


def zobrazit_ukoly(seznamUkolu):
    print("Seznam úkolů:")
    i1 = 0

    for nazevAPopisUkolu in seznamUkolu:
        i1 = i1 + 1
        nazevUkolu = nazevAPopisUkolu["nazevUkolu"]
        popisUkolu = nazevAPopisUkolu["popisUkolu"]

        text = str(i1) + ". " + nazevUkolu + " - " + popisUkolu

        print(text)


def odstranit_ukol(seznamUkolu):

    hodnExp = input("Zadejte nazev ukolu, ktery chcete odstranit : ")
    klicExp = "nazevUkolu"

    indUkolu = vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp) - 1

    if(indUkolu == -2):
        print("\nCHYBA\nTento nazev ukolu neexistuje.\nUkol nemuze byt odebran.")
    else:
        seznamUkolu.pop(indUkolu)
        print("Ukol " + hodnExp + " byl odebran")


    return(seznamUkolu)


def vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp):

    i = 0
    ind = -1

    for nazvyUkolu in seznamUkolu:
        nazevUkolu = nazvyUkolu[klicExp]
        i = i + 1
        if(nazevUkolu == hodnExp):
            ind = i
            break

    return(ind)


def vstup_uzivatele_validace():

    cislo_Ukolu = input("Vyberte možnost (1-4) : ")

    vstup_je_cislo = cislo_Ukolu.isnumeric()
    if(vstup_je_cislo == False):
        print("\nCHYBA:\nNezadali jste ciselnou hodnotu mezi 1-4! Zadejte vstup znovu.")

        # volam metodu rekurzivně
        vrat_cislo_ukolu = vstup_uzivatele_validace()
    else:
        cislo_Ukolu_int = int(cislo_Ukolu)
        if(cislo_Ukolu_int < 1) or (cislo_Ukolu_int > 4):
            print("\nCHYBA:\nVstup je mimo rozsah 1-4! Zadejte vstup znovu.")

            # volam metodu rekurzivně
            vrat_cislo_ukolu = vstup_uzivatele_validace()
        else:
            vrat_cislo_ukolu = cislo_Ukolu

    return(vrat_cislo_ukolu)


def vstup_uzivatele_a_vetveni_programu():
    seznamUkolu = []
    pokracujVCyklu = True

    while pokracujVCyklu == True:

        cislo_Ukolu = vstup_uzivatele_validace()

        match cislo_Ukolu:

            case "1":
                seznamUkolu = pridatUkol(seznamUkolu)
            case "2":
                zobrazit_ukoly(seznamUkolu)
            case "3":
                seznamUkolu = odstranit_ukol(seznamUkolu)
            case "4":
                pokracujVCyklu = False



hlavni_menu()
vstup_uzivatele_a_vetveni_programu()






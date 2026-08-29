
#import pydoc

def hlavni_menu():

    print("\nSprávce úkolů - Hlavní menu")

    ukoly = []
    ukoly.append("1. Přidat nový úkol")
    ukoly.append("2. Zobrazit všechny úkoly")
    ukoly.append("3. Odstranit úkol")
    ukoly.append("4. Konec programu")

    for typUkolu in ukoly:
        print(typUkolu)


def pridatUkol(seznamUkolu):
    nazevUkolu = input("Zadejte nazev ukolu : ")
    validaceNazevUkolu = validace_novy_ukol(nazevUkolu)

    if(validaceNazevUkolu == True):
        popisUkolu = input("Zadejte popis ukolu : ")

        nazevAPopisUkolu = {
              "nazevUkolu": nazevUkolu,
              "popisUkolu": popisUkolu
        }

        seznamUkolu.append(nazevAPopisUkolu)

        print("Úkol '" + nazevUkolu + "' byl přidán\n")

    else:
        napis_hlasku_pokud_je_validace_neplatna(nazevUkolu)

    return (seznamUkolu)


def napis_hlasku_pokud_je_validace_neplatna(nazevUkolu):

    nazevUkoluBezMezer = nazevUkolu.strip()

    print("\nÚkol nebyl přidán")

    if(nazevUkoluBezMezer == ""):
        print("Nebyl zadán žádný název úkolu, akci opakuj znovu")
    else:
        print("název ukolu by měl obsahovat alespoň jedno pismeno")


def zobrazit_ukoly(seznamUkolu):
    print("\nSeznam úkolů:")
    i1 = 0

    for nazevAPopisUkolu in seznamUkolu:
        i1 = i1 + 1
        nazevUkolu = nazevAPopisUkolu["nazevUkolu"]
        popisUkolu = nazevAPopisUkolu["popisUkolu"]

        text = str(i1) + ". " + nazevUkolu + " - " + popisUkolu

        print(text)


def odstranit_ukol(seznamUkolu):

    hodnExp = input("Zadejte nazev ukolu, ktery chceš odstranit (můžeš zadat i jeho číslo): ")
    nazevUkoluJeCislo = hodnExp.isnumeric()

    if(nazevUkoluJeCislo == False):

        klicExp = "nazevUkolu"
        indUkolu = vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp) - 1

        if(indUkolu == -2):
            print("\nCHYBA\nTento nazev ukolu neexistuje.\nUkol nemuze byt odebran.")
        else:
            seznamUkolu.pop(indUkolu)
            print("Ukol '" + hodnExp + "' byl odebrán")

    else:
        indUkolu = int(hodnExp) - 1

        if(indUkolu > len(seznamUkolu) or indUkolu < 0):
            print("\nCHYBA\nToto cislo ukolu neexistuje.\nUkol nemuze byt odebran.")

        else:
            seznamUkolu.pop(indUkolu)
            print("Ukol číslo : '" + hodnExp + "' byl odebrán")

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


# nazev ukolu nesmi obsahovat
def validace_novy_ukol(nazevUkolu):

    nazevUkoluJeCislo = nazevUkolu.isnumeric()

    if(nazevUkoluJeCislo == False):

        lowerCase = nazevUkolu.lower()
        upperCase = nazevUkolu.upper()

        if(lowerCase != upperCase):
            validaceOK = True
        else:
            validaceOK = False

    else:
        validaceOK = False


    return(validaceOK)


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
    indCyklu = 0

    while pokracujVCyklu == True:

        if(indCyklu > 0):
            hlavni_menu()

        cislo_Ukolu = vstup_uzivatele_validace()

        match cislo_Ukolu:

            case "1":
                seznamUkolu = pridatUkol(seznamUkolu)
            case "2":
                zobrazit_ukoly(seznamUkolu)
            case "3":
                seznamUkolu = odstranit_ukol(seznamUkolu)
            case "4":
                print("KONEC PROGRAMU")
                pokracujVCyklu = False


        indCyklu = indCyklu + 1


hlavni_menu()
vstup_uzivatele_a_vetveni_programu()

#pydoc.writedoc("main")
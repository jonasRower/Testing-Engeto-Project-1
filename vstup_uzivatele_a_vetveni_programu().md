[a_link](vstup_uzivatele_a_vetveni_programu()) <br>
funkce se zeptá na možnosti, dle hlavního_menu() <br>
program se ptá do doby, dokud užibvatel nezadá vstup "4"
funkce uchovává promennou seznamUkolu = []
Dle zadaného vstupu se volá jedna z následujících metod:
1: seznamUkolu = [a_link](pridatUkol(seznamUkolu))
2: [a_link](zobrazit_ukoly(seznamUkolu))
3: seznamUkolu = [a_link](odstranit_ukol(seznamUkolu))
4: vypíše jen "KONEC PROGRAMU"

seznam volaných metod:
hlavniMenu()
cislo_Ukolu = [a_link](vstup_uzivatele_validace())
seznamUkolu = [a_link](pridatUkol(seznamUkolu))
[a_link](zobrazit_ukoly(seznamUkolu))
seznamUkolu = [a_link](odstranit_ukol(seznamUkolu))

[a_link](pridatUkol(seznamUkolu))
zeptá se na název úkolu
overuje název úkolu, zda obsahuje platné znaky - pomocí metody
validaceNazevUkolu = [a_link](validace_novy_ukol(nazevUkolu))

pokud je validace v porádku, pak zapíše data do slovníku
nazevAPopisUkolu = {
              "nazevUkolu": nazevUkolu,
              "popisUkolu": popisUkolu
}

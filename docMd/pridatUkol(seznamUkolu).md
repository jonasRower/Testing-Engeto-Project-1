# pridatUkol(seznamUkolu)<br>
## Popis Funkce<br>
zeptá se na název úkolu<br>
overuje název úkolu, zda obsahuje platné znaky - pomocí metody<br>
validaceNazevUkolu = [validace_novy_ukol(nazevUkolu)](./validace_novy_ukol(nazevUkolu).md)<br>
<br>
pokud je validace platná, pak zapíše data do slovníku<br>
nazevAPopisUkolu = {<br>
              "nazevUkolu": nazevUkolu,<br>
              "popisUkolu": popisUkolu<br>
}<br>
<br>
pokud je validace neplatná, pak volá funkci [napis_hlasku_pokud_je_validace_neplatna(nazevUkolu)](./napis_hlasku_pokud_je_validace_neplatna(nazevUkolu).md)<br>
<br>
Tato funkce vrací aktualizovaný seznam úkolu zpet do [vstup_uzivatele_a_vetveni_programu()](./vstup_uzivatele_a_vetveni_programu().md)<br>
<br>
<br>
## Testovací scénár<br>
[zobrazit_ukoly(seznamUkolu)](./zobrazit_ukoly(seznamUkolu).md)

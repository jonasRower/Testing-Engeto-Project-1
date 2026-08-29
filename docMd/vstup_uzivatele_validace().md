# vstup_uzivatele_validace()<br>
## Popis Funkce<br>
funkce overuje (validuje typ vstupu)<br>
pokud není vstup císlo, pak vypíše:<br>
"Nezadali jste ciselnou hodnotu mezi 1-4! Zadejte vstup znovu." , pak se volá metoda sama sebe znovu (rekurzivne)<br>
<br>
Pokud je funkce sice císlo, ale je menší než 1 a vetší než 4, pak vypíše zprávu:<br>
"Vstup je mimo rozsah 1-4! Zadejte vstup znovu."<br>
<br>
Pokud není ani jedna podmínka splnena, pak je funkce ukoncena s návratovou hodnotou císla možnosti, dle nabídky v [hlavni_menu()](./hlavni_menu().md)<br>
<br>
## Testovací scénár<br>
Test: Validace vstupu<br>
## <br>
### Popis testu<br>
Otevrít cmd.exe<br>
Spustit program main.py<br>
<br>
Po výzve "Vyberte možnost (1-4) :" vložit postupne vstupy:<br>
<br>
Vložit Enter<br>
Vložit 123456789 + Enter<br>
Vložit ABCDEFGHIJKLMNOPQRSTUVWXYZ + Enter<br>
Vložit %?_/*~+-@&;,.][}{ + Enter<br>
<br>
<br>
### Ocekávaný výstup:<br>
Vyberte možnost (1-4) :<br>
<br>
CHYBA:<br>
Nezadali jste ciselnou hodnotu mezi 1-4! Zadejte vstup znovu.<br>
Vyberte možnost (1-4) : 123456789<br>
<br>
CHYBA:<br>
Vstup je mimo rozsah 1-4! Zadejte vstup znovu.<br>
Vyberte možnost (1-4) : ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
<br>
CHYBA:<br>
Nezadali jste ciselnou hodnotu mezi 1-4! Zadejte vstup znovu.<br>
Vyberte možnost (1-4) : %?_/*_@&;,.][}{<br>

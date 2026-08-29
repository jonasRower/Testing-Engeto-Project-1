# napis_hlasku_pokud_je_validace_neplatna(nazevUkolu)<br>
## Popis Funkce<br>
napíše zprávu pokud byl zadán neplatný název úkolu a  to jedna z následujících možností:<br>
<br>
Nebyl zadán žádný název úkolu, akci opakuj znovu<br>
nebo<br>
název ukolu by mel obsahovat alespon jedno pismeno<br>
<br>
Funkce nevrací nic, je vsak volaná z [pridatUkol(seznamUkolu)](./pridatUkol(seznamUkolu).md)<br>
<br>
<br>
## Testovací scénár<br>
Test : Pridání úkolu s neplatným názvem<br>
[automatizovaný test](../AutomatickeTesty/pridatUkol-.au3)<br>

<br>
### Popis testu<br>
Otevrít cmd.exe<br>
Spustit program main.py<br>
<br>
Vybrat možnost: 1<br>
Zadat název úkolu: {ENTER}<br>
<br>
Vybrat možnost: 1<br>
Zadat název úkolu: %<br>
<br>
Vybrat možnost: 1<br>
Zadat název úkolu: 1<br>
<br>
<br>
### Ocekávaný výstup:<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 1<br>
Zadejte nazev ukolu :<br>
<br>
Úkol nebyl pridán<br>
Nebyl zadán žádný název úkolu, akci opakuj znovu<br>
<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 1<br>
Zadejte nazev ukolu : %<br>
<br>
Úkol nebyl pridán<br>
název ukolu by mel obsahovat alespon jedno pismeno<br>
<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 1<br>
Zadejte nazev ukolu : 1<br>
<br>
Úkol nebyl pridán<br>
název ukolu by mel obsahovat alespon jedno pismeno<br>

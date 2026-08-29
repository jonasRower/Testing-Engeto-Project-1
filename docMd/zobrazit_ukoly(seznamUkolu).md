# zobrazit_ukoly(seznamUkolu)<br>
## Popis Funkce<br>
zobrazí seznam úkolu a jejich popis<br>
je volana z [vstup_uzivatele_a_vetveni_programu()](./vstup_uzivatele_a_vetveni_programu().md) pokud uzivatel zada volbu 2<br>
<br>
<br>
## Testovací scénár<br>
Test : Zobrazit seznam úkolu<br>
[automatizovaný test](../AutomatickeTesty/ZobrazitUkoly.au3)<br>

<br>
<br>
### Popis testu<br>
Otevrít cmd.exe<br>
Spustit program main.py<br>
<br>
<br>
Vybrat možnost: 1<br>
Zadat název úkolu : Ukol 1<br>
Zadat popis úkolu : Popis 1<br>
<br>
Vybrat možnost: 1<br>
Zadat název úkolu : Ukol 2<br>
Zadat popis úkolu : Popis 2<br>
<br>
Vybrat možnost: 1<br>
Zadat název úkolu : Ukol 3<br>
Zadat popis úkolu : Popis 3<br>
<br>
<br>
Vybrat možnost: 2<br>
<br>
<br>
### Ocekávaný výstup:<br>
Seznam úkolu:<br>
1. Ukol 1 - Popis 1<br>
2. Ukol 2 - Popis 2<br>
3. Ukol 3 - Popis 3<br>

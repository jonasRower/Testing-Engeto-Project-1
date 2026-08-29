# odstranit_ukol(seznamUkolu)<br>
## Popis Funkce<br>
je možné zadat bud název nebo císlo úkolu, který bude odebrán<br>
pokud je zadán název úkolu, pak zjištuji jeho index (v seznamu) pomocí funkce:<br>
indUkolu = [vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp)](./vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp).md) - 1<br>
<br>
po zjištení indexu (bud zadaného jeho císla úkolu, nebo názvu) odebírám úkol pomocí metrody seznamUkolu.pop(indUkolu)<br>
<br>
vrací aktualizovaný seznam nazpet do [vstup_uzivatele_a_vetveni_programu()](./vstup_uzivatele_a_vetveni_programu().md)<br>
<br>
<br>
## Testovací scénár<br>
Test : Odebrání úkolu zadaného pomocí jeho císla<br>
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
Vybrat možnost: 3<br>
Zadat vstup: 1<br>
<br>
Vybrat možnost: 2<br>
<br>
<br>
### Ocekávaný výstup:<br>
Zadejte nazev ukolu, ktery chceš odstranit (mužeš zadat i jeho císlo): 1<br>
Ukol císlo : '1' byl odebrán<br>
<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 2<br>
<br>
Seznam úkolu:<br>
1. Ukol 2 - Popis 2<br>
2. Ukol 3 - Popis 3<br>

<br>
## Testovací scénár<br>
Test : Odebrání úkolu zadaného pomocí jeho názvu<br>
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
Vybrat možnost: 3<br>
Zadat vstup: Ukol 1<br>
<br>
Vybrat možnost: 2<br>
<br>
<br>
### Ocekávaný výstup:<br>
Zadejte nazev ukolu, ktery chceš odstranit (mužeš zadat i jeho císlo): Ukol 1<br>
Ukol 'Ukol 1' byl odebrán<br>
<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 2<br>
<br>
Seznam úkolu:<br>
1. Ukol 2 - Popis 2<br>
2. Ukol 3 - Popis 3<br>

<br>
## Testovací scénár<br>
Test: Nevalidní vstup - odebírám císlo úkolu, které neexistuje<br>
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
Vybrat možnost: 3<br>
Zadat vstup: 99  (neexistující císlo úkolu)<br>
<br>
Vybrat možnost: 2<br>
<br>
<br>
### Ocekávaný výstup:<br>
Vyberte možnost (1-4) : 3<br>
Zadejte nazev ukolu, ktery chceš odstranit (mužeš zadat i jeho císlo): 99<br>
<br>
CHYBA<br>
Toto cislo ukolu neexistuje.<br>
Ukol nemuze byt odebran.<br>
<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 2<br>
<br>
Seznam úkolu:<br>
1. Ukol 1 - Popis 1<br>
2. Ukol 2 - Popis 2<br>
3. Ukol 3 - Popis 3<br>

<br>
## Testovací scénár<br>
Test : Nevalidní vstup - odebírám název úkolu, které neexistuje<br>
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
Vybrat možnost: 3<br>
Zadat vstup: xxx<br>
<br>
Vybrat možnost: 2<br>
<br>
<br>
### Ocekávaný výstup:<br>
Zadejte nazev ukolu, ktery chceš odstranit (mužeš zadat i jeho císlo): xxx<br>
<br>
CHYBA<br>
Tento nazev ukolu neexistuje.<br>
Ukol nemuze byt odebran.<br>
<br>
Správce úkolu - Hlavní menu<br>
1. Pridat nový úkol<br>
2. Zobrazit všechny úkoly<br>
3. Odstranit úkol<br>
4. Konec programu<br>
Vyberte možnost (1-4) : 2<br>
<br>
Seznam úkolu:<br>
1. Ukol 1 - Popis 1<br>
2. Ukol 2 - Popis 2<br>
3. Ukol 3 - Popis 3<br>

## odstranit_ukol(seznamUkolu)<br>
je možné zadat bud název nebo císlo úkolu, který bude odebrán<br>
pokud je zadán název úkolu, pak zjištuji jeho index (v seznamu) pomocí funkce:<br>
indUkolu = [vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp)](./vrat_Index_Dle_Klice(seznamUkolu, klicExp, hodnExp).md) - 1<br>
<br>
po zjištení indexu (bud zadaného jeho císla úkolu, nebo názvu) odebírám úkol pomocí metrody seznamUkolu.pop(indUkolu)<br>
<br>
vrací aktualizovaný seznam nazpet do [vstup_uzivatele_a_vetveni_programu()](./vstup_uzivatele_a_vetveni_programu().md)<br>

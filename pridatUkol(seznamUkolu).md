[a_link](pridatUkol(seznamUkolu))<br>
zeptá se na název úkolu<br>
overuje název úkolu, zda obsahuje platné znaky - pomocí metody<br>
validaceNazevUkolu = [a_link](validace_novy_ukol(nazevUkolu))<br>
<br>
pokud je validace v porádku, pak zapíše data do slovníku<br>
nazevAPopisUkolu = {<br>
              "nazevUkolu": nazevUkolu,<br>
              "popisUkolu": popisUkolu<br>
}<br>

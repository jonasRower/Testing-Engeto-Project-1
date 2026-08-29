# Testing-Engeto-Project-1

# <ins> Task manager </ins>

## Zadání




Program by měl umožnit přidávat, zobrazovat a odstraňovat úkoly. Následující části kódu jsou prázdné funkce, které musíte doplnit. Každá funkce má svůj specifický úkol, který je popsán níže. Úkoly budou ukládány do seznamu ukoly = [].

﻿
### def hlavni_menu()

Funkce hlavního menu, která poskytuje možnosti pro přidání, zobrazení a odstranění úkolu. Pokud uživatel zadá neplatnou volbu, program ho upozorní a nechá uživatele opakovat znovu volbu.


### def pridat_ukol()
Tato funkce má uživateli umožnit zadat název a popis nového úkolu a uložit jej do seznamu úkolů. Zde platí volba 1 v hlavním menu. Po zadání úkolu proggit ram pokračuje dál nabídkou hlavního menu. Při zadání prázdného vstupu do Zadejte název úkolu nebo Popis úkolu, program upozorní uživatele, že zadal prázdný vstup a nechá ho zadat název i popis znovu.

﻿﻿
## def zobrazit_ukoly()
Tato funkce má zobrazit všechny úkoly v seznamu. Zde platí volba 2 v hlavním menu. Po zobrazení úkolů program pokračuje dál nabídkou hlavního menu.
﻿
﻿
### def odstranit_ukol()
Tato funkce má uživateli umožnit zadat číslo úkolu, který chce odstranit, a tento úkol odstranit. Zde platí volba 3 v hlavním menu. Po odstranění úkolu program pokračuje dál nabídkou hlavního menu. Zde je potřeba, aby uživatel viděl všechny uložené úkoly a při výběru neexistujícího úkolu byl upozorněn.

﻿
<ins> Konec programu </ins>

Pokud uživatel zadá volbu 4 v hlavním menu program se ukončí.
﻿

o 1 a potvrďte stisknutím klávesy Enter.
Očekávaný výsledek: Program spustí funkci pridat_ukol().
Skutečný výsledek: Funkce pridat_ukol() byla spuštěna a program zobrazil výzvu k zadání nového úkolu
Stav: Pass
Poznámky: Tento případ je důležitý, protože ověřuje základní navigaci z hlavního menu a funkčnost jedné z klíčových funkcí programu.
<br>
<br>

### Dokumentace kódu & testů
[dokumentace kódu a testů](./docMd/hlavni_menu().md) je zde
<br>
<br>

## Automatické testy
Automatické testy odpovídají testům manuálním. Jsou psané v jazyce AutoIt. Sckript AutoIT (.au3) otevře cmd.exe, spustí program a zadává požadované vstupy. Výstup programu nakopíruje do txt. souboru <br>
Pokud by testy nešly, je potřeba upravit dobu čekání pomocí funkcí sleep(time), kde time je čas v milisekundách




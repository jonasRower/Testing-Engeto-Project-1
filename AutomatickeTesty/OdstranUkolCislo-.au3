run ("cmd.exe")
Sleep(500)


send("cd Testing-Engeto-Project-1" & "{ENTER}")
send("main.py" & "{ENTER}")

;pocka nez otevre program
Sleep(1000)

;######  PROGRAM #######
;zada ukol 1
send("1" & "{ENTER}")
send("Ukol 1" & "{ENTER}")
send("Popis 1" & "{ENTER}")

;zada ukol 2
send("1" & "{ENTER}")
send("Ukol 2" & "{ENTER}")
send("Popis 2" & "{ENTER}")

;zada ukol 3
send("1" & "{ENTER}")
send("Ukol 3" & "{ENTER}")
send("Popis 3" & "{ENTER}")

;zobrazi vsechny ukoly
send("2" & "{ENTER}")

;odstrani ukol
send("3" & "{ENTER}")
send("99" & "{ENTER}")

;zobrazi zbyvajici ukoly
send("2" & "{ENTER}")

;###### zkopiruje vystup do txt #######
send("^+m")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")
send("+{UP}")

Sleep(800)

send("^c")
run ("notepad.exe")

Sleep(800)
send("^N")

Sleep(500)
send("^v")

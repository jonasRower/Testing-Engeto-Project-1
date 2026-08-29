run ("cmd.exe")
Sleep(500)


send("cd Testing-Engeto-Project-1" & "{ENTER}")
send("main.py" & "{ENTER}")


;pocka nez otevre program
Sleep(1000)

;######  PROGRAM #######
;zada prazdny vstup
send("{ENTER}")

;zada ciselny vstup
send("123456789" & "{ENTER}")

;zada vstup znaku abecedy
send("ABCDEFGHIJKLMNOPQRSTUVWXYZ" & "{ENTER}")

;zada vstup znaku mimo abecedy
send("%?_/*~+-@&;,.][}{" & "{ENTER}")


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

Sleep(800)

send("^c")
run ("notepad.exe")

Sleep(800)
send("^N")

Sleep(500)
send("^v")
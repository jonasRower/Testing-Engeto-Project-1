run ("cmd.exe")
Sleep(500)


send("cd Testing-Engeto-Project-1" & "{ENTER}")
send("main.py" & "{ENTER}")


;pocka nez otevre program
Sleep(1000)

;######  PROGRAM #######
;zada prazdny vstup
send("4")

Sleep(100)
send("{ENTER}")


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


Sleep(800)

send("^c")
run ("notepad.exe")

Sleep(800)
send("^N")

Sleep(500)
send("^v")
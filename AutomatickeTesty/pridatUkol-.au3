run ("cmd.exe")
Sleep(500)


send("cd Testing-Engeto-Project-1" & "{ENTER}")
send("main.py" & "{ENTER}")

;pocka nez otevre program
Sleep(1000)

;######  PROGRAM #######
;zada ukol 1
send("1" & "{ENTER}")
send("{ENTER}")

;zada ukol 2
send("1" & "{ENTER}")
send("%" & "{ENTER}")

;zada ukol 3
send("1" & "{ENTER}")
send("1" & "{ENTER}")


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
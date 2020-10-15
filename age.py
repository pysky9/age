driving = input("請問你有開過車嗎? ")
if driving != "有" or driving != "沒有" :
	print("只可以輸入 有/沒有")
	raise SystemExit

age = eval(input("請問你的年齡?"))
if driving == "有" :
	if age >= 18 :
		print("你通過測驗了")
	else :
		print("你怎會開過車?")
elif driving == "沒有" :
	if age >= 18 :
		print("你可以去考駕照了")
	else :
		print("再過幾年你就可以考駕照了")
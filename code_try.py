code = "a123456"
n = 3
while n > 0:
	enter = input("請輸入密碼")
	if enter == code:
		print("登入成功！")
		break
	else:
		n = n - 1
		print("密碼錯誤，你還有",n,"次機會")


if n == 0:
	print("連續三次錯誤，請與客服人員聯繫")

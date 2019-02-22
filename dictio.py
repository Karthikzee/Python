dic = {"a":1, "b":2, "c":3, "c":4, "d":5}
for i in dic:
	n = input("give a alphabet from a to d")
	if n in dic:
	 	print(n, "is the", dic[i], "letter in alphabet")
	else:
		print("try entering alphabets from a to d")



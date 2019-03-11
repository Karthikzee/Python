#3. handling zero error
try:
	a = int(input("number"))
	if a <= 3:
		b = a/(a-3)
		b = float(b)
		print(b)

except:
	print("IndexError")
#except
try:
	name = int(input("Give a number: "))
	print(name)
except:
	print("Type error")
else:
	print("is the number")
finally:
	print("done")

#except with raise
try:
	num = int(input("Give a number: "))
	print(num)
	raise ValueError
except ValueError:
	print("Invalid input")


import random

d = 6
x = input("Press r to roll the dice \n Press q to quit\n")
if x == "r":
	print("You got:",d)
	d = 2

x = input("Press r to roll the dice \n Press q to quit\n")
if x == "r":
	print("You got:",d)
	d = 3

x = input("Press r to roll the dice \n Press q to quit\n")
if x == "r":
	print("You got:",d)
	d = 6

x = input("Press r to roll the dice \n Press q to quit\n")
if x == "r":
	print("You got:",d)
	d = 2

x = input("Press r to roll the dice \n Press q to quit\n")
if x == "r":
	print("You got:",d)
	d = 3
x = input("Press r to roll the dice \n Press q to quit\n")
if x == "r":
	print("You got:",d)

print("hooray, you won!")

if x == "q":
	print("THE END")
	quit()

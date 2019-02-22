import random

while True:
	x = input("Press r to roll the dice \n Press q to quit\n")
	if x == "r":
		print("You got:",random.randint(1,6))
	if x == "q":
		print("THE END")
		quit()
		

import random

dice_value = 0
position = 0

while True:
	roll = input("Press r to roll\nPress q to quit")

	if roll == "r":
		dice_value = random.randint(1,6)
		print("You got:", dice_value)

	if roll == "q":
		print("Thank you")
		quit()

	if dice_value == 1 or dice_value == 6:
		position = dice_value
		break

print("Congratulations! You are in the game.\nYou're at:", dice_value)


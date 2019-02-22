import random

d = 0
p = 0

def roll():
	return random.randint(1,6)

while True:
	menu = input("Press r to roll and q to quit")
	if menu == "r":
		d = roll()
		print("You got ", d)
	if menu == "q":
		print("Thank you")
		quit()

	if d == 1 or d == 0:
		p = p+d
		print("Congratulations! You are int the game.")
		print ("you are at positon", p)
		break

while True:
	menu = input("Press r to roll again")

	if menu == "r":
		d = roll()
		print("You got:", d)
		p = p+d

		if p ==100:
			print("Hurray! You won the game")
			exit()

		if p>100:
			p= p-d
			print("You should get ", p-d,"or less to make a move!")

		if p == 8:
			p = 37
			print("Lucky you climbed to", p)

		if p == 13:
			p = 34
			print("Lucky you climbed to", p)

		if p == 40:
			p = 68
			print("Lucky you climbed to", p)

		if p == 52:
			p = 81
			print("Lucky you climbed to", p)

		if p == 76:
			p = 97
			print("Lucky you climbed to", p)

		if p == 38:
			p = 9
			print("ouch that snake drowned you to", p)

		if p == 25:
			p = 4
			print("ouch that snake drowned you to", p)

		if p == 11:
			p = 2
			print("ouch that snake drowned you to", p)

		if p == 65:
			p = 46
			print("ouch that snake drowned you to", p)

		if p == 93:
			p = 64
			print("ouch that snake drowned you to", p)

		if p == 89:
			p = 70
			print("ouch that snake drowned you to", p)

		print("you are at", p)
#rock paper scissors game
#calling random module for choosing a string from tuple using .choice function
import random

a = ["rock", "papers", "scissors"]
w = "you win"
l = "you lose"
u = 0
c = 0
count = 0
#loop to play again and again
while count < 6:
	#player will type in their desired option
	p = input("enter rock or papers or scissors")
	#contional statement to quit
	if p == "q":
		print("thanks for playing")
		quit()
	#computer will choose in random
	com = random.choice(a)
	print("you chose", p, "computer chose", com)
	#comparing player and compter options and displaying who wins
	if p == com:
		print("its a tie")
	elif p == "rock" and com == "scissors":
		print(w)
		u = u+1
	elif p == "papers" and com == "rock":
		print(w)
		u = u+1
	elif p == "scissors" and com == "papers":
		print(w)
		u = u+1
	elif p == "scissors" and com == "rock":
		print(l)
		c = c+1
	elif p == "rock" and com == "papers":
		print(l)
		c = c+1
	elif p == "papers" and com == "scissors":
		print(l)
		c = c+1
	print ("Your score ", u, "computers score is", c)
	count = count + 1
if count == 6:
	if u > c:
		print("You win the game")
	else:
		print("Computer wins the game")
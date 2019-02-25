#rock paper scissors game
#calling random module for choosing a string from tuple using .choice function
import random

a = ["rock", "papers", "scissors"]
u = "you win"
l = "you lose"
#loop to play again and again
while True:
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
		print(u)
	elif p == "papers" and com == "rock":
		print(u)
	elif p == "scissors" and com == "papers":
		print(u)
	elif p == "scissors" and com == "rock":
		print(l)
	elif p == "rock" and com == "papers":
		print(l)
	elif p == "papers" and com == "scissors":
		print(l)
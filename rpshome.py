#rock paper scissors game
#calling random module for choosing a string from tuple using .choice function

import random

a = ("rock", "papers", "scissors")

#loop to play again and again
while True:
    #player will type in their desired option
    player = input("Type rock or papers or scissors: ")
    #computer will choose in random
    com = random.choice(a)
    #checking if player input a valid option
    if player == "rock" or player == "papers" or player == "scissors":
        print("Computer chose", com, "and You chose", player)
        #comparing player and compter options and displaying who wins
        if (player == "rock" and com == "scissors") or (player == "papers" and com == "rock") or (player == "scissors" and com == "papers"):
            print("Hoo rey! you win.")
        elif (player == "scissors" and com == "rock") or (player == "rock" and com == "papers") or (player == "papers" and com == "scissors"):
            print("Ouch! computer wins.")
        elif player == com:
            print("Lol! it's a tie.")
    #prompt the user to give a valid option
    else:
        print("Give a valid input.")
    continue

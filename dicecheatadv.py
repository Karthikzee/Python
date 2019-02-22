import random

i = 0
while i < 2:
	d = (6)

	r = input("press r to roll, q to quit")
	if r =="r":
		print("you got ", d)
		d = int(d/3)

	r = input("press r to roll, q to quit")
	if r =="r":
		print("you got ", d)
		d = d+1

	r = input("press r to roll, q to quit")
	if r =="r":
		print("you got ", d)
		d = d/2
	i = i + 1
print ("hooray, you won!")
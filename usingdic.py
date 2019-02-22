import random

d = {22:1, 43:5, 67:89, 56:78, 98:67, 76:6, 87:26}

p = random.choice([22, 43, 67, 56, 98, 76, 87])

print("you got", p)

if p > d[p]:
	print("its a snake")
else:
	print("its a ladder")
print("u go to", d[p])
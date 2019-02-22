#elements in tuple cannot be changed
lis = ("helo", "36", "popo", 454.2)

print(lis)

for e in range(2,4):
	print(lis[e])

lis[2]= "nope"

for e in range(4):
	print(lis[e])

print(lis)

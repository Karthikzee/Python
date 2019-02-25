#1
lis1 = []
print (lis1)
#2
lis2 = [1, 2, 3, "a", "b", "c"]
print(lis2)
#12
print(lis2[3])
#3
for e in lis2:
	print(e)
#4 
for e in range(1,5):
	print(e)
#5
lis2[5] = "aa"
print(lis2)
#6
l = len(lis2)
print(l)
#7
if 2 in lis2:
	print("True")
#8
lis2.append(8)
print (lis2)
#9
import random
r = random.randint(1,3)
print (r)
#10
c = random.choice(lis2)
print (c)
#11
i = input("say something: ")
print (i)

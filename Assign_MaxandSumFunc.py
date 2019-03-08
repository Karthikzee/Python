#1 finding max of three values
def maxi(a, b, c):
	if (a>b) and (a>c):
		return a

	elif (b>a) and (b>c):
		return b

	else:
		return c

a= input("First number: ")
b= input("Second number: ")
c= input("Third number: \n")

m= maxi(a, b, c)
print(m, "is the largest number\n")

#2 sum of numbers of list
def sum_list(a):
	i = 0
	for e in a:
		i = i+e
	return i

a = []
n= int(input("Number of element in list"))

for k in range(n):
	el = int(input("Give the elements of list"))
	a.append(el)

i = sum_list(a)

print(i, "is the sum of list")





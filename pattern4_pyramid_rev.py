# program to print a reversed pyramid pyramid like pattern

n = int(input("Number of stacks: "))

s = 0
for i in range(1, n+1):
	print(' '*s, end='')
	s +=1
	print('* '*n)
	n = n - 1
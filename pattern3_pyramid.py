# program to print a pyramid like pattern

n = int(input("Number of stacks: "))
s = n-1 #spaces

for i in range(1, n+1):
    print(" "*s, end="")
    s -=1
    print("* "*i)
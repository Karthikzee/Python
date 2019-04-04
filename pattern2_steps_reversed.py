# program to print a reversed steps like pattern

n = int(input("Number of stacks: "))

for i in range(1, n+1):
    print("* "*n)
    n -= 1
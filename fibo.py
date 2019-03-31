# fibonacci series
n = int(input("Enter term till fib series should continue: "))
a = 0
b = 1
if n <= 0:
    print("Invalid")
else:
    while a <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c


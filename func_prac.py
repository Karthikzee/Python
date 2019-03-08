#1.function with no parameter

def func1():
	print("blanced")
	print("as all things")
	print("should be!\n")

func1()

#2. function with one parameter
def func2(i):
	x = i * 3
	print(x, "\n")

func2(2)

#3. function with more parameters
def func3(name, height, weight):
	bmi = (height+weight)/2
	print(name, "bmi is", bmi, "\n")

func3("ken", 2, 50)

#4. function with default parameter
def func4(name = "ken", age = 7):
	print(name, "of age", age, "is a good student\n")

func4("ravi", 8)
func4()
func4(7)

#5. function with return value
def func5(a, b):
	c = a + b
	return(c)

d = func5(45, 50)
print(d)

#6. function calling function
def func6(x):
	e = func5(8, 9)
	f=e*x
	return f

g = func6(5)
print(g)


import matplotlib.pyplot as plt
import csv
filename = "sheet1.csv"

x = []
y = []
 
with open(filename, 'r') as csvfile: 
	csvreader = csv.reader(csvfile, delimiter=",")

	for row in csvreader:
		x.append(int(row[0])) 
		y.append(int(row[1]))

plt.bar(x, y, color='b')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plotting from csv data")

plt.show()

#plotting a graph using data of a CSV file
import matplotlib.pyplot as plt
import csv

#file location of the csv file
filename = "D:\Sheet1.csv"

x = []
y = []

#opening csv file to read
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#iterating over the objects in csv file 
    for row in csvreader:
        x.append(int(row[0]))
        y.append(int(row[1]))
#adding color,size and style to marker and line 
plt.plot(x, y, color='b', linestyle='-', marker='o', markerfacecolor='g', markersize=5)

#naming the axis and the graph
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plotting from csv data")

plt.show()

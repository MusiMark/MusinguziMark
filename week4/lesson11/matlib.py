import matplotlib.pyplot as plt
import numpy as np

# line Graph
x = [0,2,4,8,10]
y=[0,4,8,16,36]

fig, ax = plt.subplots()

ax.plot(x,y,marker='o',label='Data Points' ,color='red' ,linestyle='--')

ax.set_title('Basic Line Graph')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

ax.legend()
plt.show()

#Simple Bar Chart
import matplotlib.pyplot as plt
w = ['John', 'Peter', 'Ruth', 'Simon', 'Samuel' ]
z =[20,30,40,50,20]

plt.bar(w,z)
plt.title("Simple Bar Graph")
plt.xlabel('Names of students')
plt.ylabel("Age of the students")

plt.show()

# histogram
data = np.random.randint(1, 1000, size=200)
plt.hist(data)
plt.title("Histogram of data")
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.show()

# piechart
pie_data = [98,34,76,26,50]
pie_labels = ['Label1','Label2','Label3','Label4','Label5']

plt.pie(pie_data, labels=pie_labels)
plt.legend()
plt.show()

# scatter
scatter_data = np.random.randint(1, 10001, size=2000)

first_half, second_half = np.split(scatter_data, 2)

plt.title('A Simple Scatter Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.scatter(first_half, second_half)
plt.show()

# boxpolt
box_data = np.random.randint(1, 100, size=100)

plt.boxplot(box_data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()

# heat map
heat_data = np.random.randint(1, 100, size=(10, 10))
print(heat_data)
plt.imshow(heat_data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Values')
plt.title("Heat Map")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()
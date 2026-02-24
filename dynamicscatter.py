import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))

x = []
y = []

for i in range(n):
    x_value = float(input(f"Enter x value for point {i+1}: "))
    y_value = float(input(f"Enter y value for point {i+1}: "))
    
    x.append(x_value)
    y.append(y_value)

plt.figure()
plt.scatter(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("User Input Scatter Plot")

plt.grid(True)
plt.show()
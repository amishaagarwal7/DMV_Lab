import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50, 60]
y = [15, 25, 35, 45, 55, 65]

plt.figure()
plt.scatter(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Scatter Plot")

plt.show()
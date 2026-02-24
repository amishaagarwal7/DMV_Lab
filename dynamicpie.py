import matplotlib.pyplot as plt

n = int(input("Enter the number of categories: "))

labels = []
sizes = []

for i in range(n):
    label = input(f"Enter label for category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    sizes.append(value)

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("User Input Pie Chart")

# Display chart
plt.show()
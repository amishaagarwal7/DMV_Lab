import matplotlib.pyplot as plt
n= int(input("Enter the number of categories: "))

categories=[]
values=[]

for i in range(n):
    cat= input(f"Enter the name of category {i+1}: ")
    val= int(input(f"Enter the value for {cat}: "))
    categories.append(val)
    values.append(val)

plt.bar(categories, values)

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Dynamic Bar Chart (User Input)")

plt.show()
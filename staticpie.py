import matplotlib.pyplot as plt

# Data defined in the code
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]

# Create pie chart
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add title
plt.title("Programming Language Popularity")

# Display the chart
plt.show()
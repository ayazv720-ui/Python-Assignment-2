import matplotlib.pyplot as plt

# Take input
n = int(input("Enter number of students: "))

names = []
marks = []

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

# Create chart
plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

# Save dashboard
plt.savefig("dashboard.png")

# Display chart
plt.show()

print("Dashboard saved successfully as dashboard.png")

import matplotlib.pyplot as plt

# Take input
n = int(input("Enter number of students: "))

names = []
marks = []

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

# Create chart
plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

# Save dashboard
plt.savefig("dashboard.png")

# Display chart
plt.show()

print("Dashboard saved successfully as dashboard.png")
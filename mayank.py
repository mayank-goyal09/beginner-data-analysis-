# Python Basics Review

# --- Variables and Data Types ---
name = "John"
age = 16
height = 5.9
is_student = True

# --- Operators ---
sum_result = age + 5
is_taller = height > 6
is_teen = age >= 13 and age <= 19

# --- Control Flow ---
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

# --- Loops ---
# For loop
for i in range(5):
    print(f"Count: {i}")

# While loop
count = 0
while count < 3:
    print("Looping...", count)
    count += 1

# --- Functions ---
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# --- Lists, Tuples, Dictionaries ---
fruits = ["apple", "banana", "cherry"]
coordinates = (4, 5)
student = {"name": "John", "age": 16, "grade": "A"}

print(fruits[1])       # Accessing list
print(coordinates[0])  # Accessing tuple
print(student["name"]) # Accessing dictionary

# --- Error Handling ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# --- Mini Task: Basic Data Analysis Example ---
import pandas as pd
import matplotlib.pyplot as plt

# Sample data simulation
data = {
    'Brand': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Units_Sold': [100, 150, 80, 120, 170, 90],
    'Unit_Price': [300, 250, 400, 310, 260, 390]
}
df = pd.DataFrame(data)

# Revenue Calculation
df['Revenue'] = df['Units_Sold'] * df['Unit_Price']

# Grouping by Brand
brand_units = df.groupby('Brand')['Units_Sold'].sum()

# Bar Chart
bars = plt.bar(brand_units.index, brand_units.values, color=['orange', 'skyblue', 'green'], edgecolor='black')
plt.xlabel('Brand')
plt.ylabel('Units Sold')
plt.title('Units Sold per Brand')

# Add labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center')

plt.show()

# Made by Carlos Corona

# Tuples

# Student named Carlos, 20 years old and degree in accounting
student = ('Carlos', 20, 'Accounting')
print(student)

# We can have different variables but we cannot modify them
name, age, degree = student
print(name)
print(age)
print(degree)

# Using zip() in lists
list_a = ['Carlos', 'Amanda', 'Leonel']
list_b = [20, 21, 23]

# Combine lists and print with list()
new_list = zip(list_a, list_b)
print(list(new_list))
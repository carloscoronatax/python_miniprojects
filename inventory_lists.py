# This .py is a bunch of practice exercises made by carloscoronatax. Enjoy!

# This projects consists in showcasing and manipulating fruits list

fruits = ['apple', 'banana', 'pear', 'watermelon', 'orange', 'peach']

# Here we are using len to give us the number of items in fruits
fruits_lenght = len(fruits)

# Print it
print(fruits_lenght)

# We want first fruit
what_is_fruit_1 = fruits[0]
print(what_is_fruit_1)

# We want sixth fruit
what_is_fruit_6 = fruits[5]
print(what_is_fruit_6)

# We want fruits between 1 and 3
fruits_between_1_and_2 = fruits[1:3]
print(fruits_between_1_and_2)

# Return number of apples in fruits
how_many_apples_are_there = fruits.count('apple')
print(how_many_apples_are_there)

# Remove pear from fruits
remove_pear_from_fruits = fruits.pop(2)
print(remove_pear_from_fruits)
print(fruits)

# Add pineapple to fruits
fruits.insert(5, 'pineapple')
print(fruits)

# Sort fruits alphabetical order
fruits.sort()
print(fruits)








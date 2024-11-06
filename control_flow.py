# This py is a bunch of practice exercises made by carloscoronatax. Enjoy!


# Start with 'hello' to make sure python working.
print('hello')

# We can see here how if, else statements work. We check if username is 'carloscoronatax'
user_name = 'carloscoronatax'

if user_name == 'carloscoronatax':
    print('Access Allowed')
else:
    print('Access Denied')

# Now, we want to try using operators, here we see that x is smaller than y.

x = 5
y = 10

if x > y:
    print('x > y')
elif x < y:
    print('x < y')
else:
    print('x == y')

# Also if we want to see if someone has enough money to buy a car, you use:

car_price = 10000

if car_price == 10000:
    print('You can buy the car')
if car_price < 10000:
    print('You dont have enough money to buy the car')

# Now we use and, or, not boolean operators. Calculate if student has the requirements to gradute.

# Student:
credits = 149
gpa = 2.5

if credits >= 150 and gpa >= 2.5:
    print('Congrats you can get your degree!')
elif credits >= 150 and gpa < 2.5:
    print('You dont have the minimum GPA')
elif credits < 150 and gpa >= 2.5:
    print('You dont have the minimum credits!')
else:
    print('Try again! :(')

# Now we use or operator. Here you need at least one requirement to graduate.

credits_1 = 149
gpa_1 = 2.1

if credits_1 >= 150 or gpa_1 >= 2.5:
    print('You have met one of the requirements!')
else:
    print('You need at least one! :(')

# Now we use not operator:

age = 20

if not age >= 21:
    print('Sorry you are too young to buy alcohol')
else:
    print('You are good to go!')



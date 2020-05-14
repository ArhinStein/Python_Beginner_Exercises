cars = ['audi', 'bmw','subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())

#These 3 dots are used for breaks.
'''
# Conditional Test
car = "bmw"
car == "bmw"
'''

requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies") 

#Numerical comparisons
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
        print("You are under age!")
print("Wait till you're 18. Thanks!")

#If-Elif-Else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


#Alternate
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else: 
    price = 10
print("Your admission cost is $" + str(price) + ".")

#Multiple Elif
age = 62
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age <65:
    price = 20
else: 
    price = 10
print("Your admission cost is $" + str(price) + ".")

#Example 01
alien_color = 'green'
if alien_color == 'green':
    point = 5
if alien_color == 'yellow':
    point = 2
if alien_color == 'red':
    point = 1
print("You just earned " + str(point) + " points!")

#Example 02
alien_color = 'green'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 10
print("You just earned " + str(point) + " points!")

#EXAMPLES OF MERGED IF_STATEMENT AND FOR_LOOP
usernames = ['john', 'ben','emma','jay','admin']
for username in usernames:
    if username == 'admin':
        print("Hello\t" + username + ", would you like to see a status report?")
    else:
        print("Hello\t" + username + ", thank you for logging in again.")

#EXAMPLES OF MERGED IF_STATEMENT AND FOR_LOOP 02
usernames = []
if username in usernames:
    for username in usernames:
        print("Hello\t" + username + ", thank you for logging in again.")
    print("\nWe've got your back always!")
else:
    print("We need to find some users!")

# Algorithm to check usernames
current_users = ['john','andrew', 'peter', 'paul', 'emma']
new_users = ['john','andrew', 'sam', 'fara', 'kim']
for new_user in new_users:
    if new_user  in current_users:
        print("User name is available, provide a new name!")
    else:
        print("Welcome to the page! " + new_user.upper())
print("\nDo yourself the favor of going through the instructions")

#Ordinal Numbers
ordinal_numbers = list(range(1,10))
print("\n\nThese are the positions:")
for value in ordinal_numbers:
    if value is 1:
        print(str(value) + "st")
    elif value is 2:
        print(str(value) + "nd")
    elif value is 3:
        print(str(value) + "rd")
    else:
        print(str(value) + "th")
print("\nThank you!")
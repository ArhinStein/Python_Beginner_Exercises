#dictionaries in Python is a collection of key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

###################################
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + "points!")

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)

################################
favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'C',
    'edward' : 'Ruby on Rails',
    'phil' : 'Python'
    }
print(favorite_languages)

###################################
'''
Looping through dictionaries
This is quite different from looping through a list
'k' and 'v' are just placeholders for the variable
'.item()' is the method to execute the dictionaries.
'''
user_o = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
    }
for k, v in user_o.items():
    print("\nK: " + k.title())
    print("V: " + v.title())

print()

#looping through just the keys:
favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'C',
    'edward' : 'Ruby on Rails',
    'phil' : 'Python'
    }
for name in favorite_languages.keys():
    print(name.title())
print()
for language in favorite_languages.values():
    print(language.title())

##############################################
#Nesting of Dictionaries
#A List of Dictionaries
alien_0 = {'color' : 'green', 'point': 5}
alien_1 = {'color' : 'yellow', 'point': 10}
alien_2 = {'color' : 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

###############################################
#A List in a Dictionary
#Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

################################################
#A Dictionary in a Dictionary
# Accessing Information of Users.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        }
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
#Creating a List
my_shopping_list = ['pen','paper','eraser','ruler']
print(my_shopping_list)

#Printing out a member in a list
print(my_shopping_list[2])
my_shopping_list[3] = 'Long Ruler'
print(my_shopping_list)
print(my_shopping_list[1:3])

#Adding an item to the list
my_shopping_list.append('compass')
my_shopping_list.insert(2, 'protractor')
my_shopping_list.sort()
print(my_shopping_list)
del my_shopping_list[2]
print(my_shopping_list)

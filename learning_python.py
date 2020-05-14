filename = 'learn_python.txt'

with open(filename) as file:
    contents = file.readlines()

for content in contents:
    print(content.rstrip())

print(' ' * 3)

#Changing the word  Python to Dart.
filename = 'learn_python.txt'

with open(filename) as file:
    contents = file.readlines()

for content in contents:
    content_change = content.replace('Python', 'Dart')
    print(content_change.rstrip())
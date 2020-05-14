# First Algorigthm
people_0 = {'name' : 'papa', 'height': 15}
people_1 = {'name' : 'ewurama', 'height': 10}
people_2 = {'name' : 'ogracious', 'height': 5}

peoples = [people_0, people_1,people_2]
for people in peoples:
    if people is people_0:
        print(people['name'].title() + " has a height of " +
        str(people['height']))
    
    elif people is people_1:
        print(people['name'].title() + " has a height of " +
        str(people['height']) + "")

    else:
        print(people['name'].title() + " has a height of " +
        str(people['height']) + "inches")

print("   ")

##############################################################
# Other Approach: Smart Way
people_0 = {'name' : 'papa', 'height': 15}
people_1 = {'name' : 'ewurama', 'height': 10}
people_2 = {'name' : 'ogracious', 'height': 5}

peoples = [people_0, people_1,people_2]
for people in peoples:
    if people is people_0:
        height = 15
    
    elif people is people_1:
        height = 10

    else:
        height = 5

    print(people['name'].title() + " has a height of " +
        str(people['height']) + " inches")

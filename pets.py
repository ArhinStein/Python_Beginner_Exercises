# Code of info about pets and their owners
biggy = {'kinda_animal': 'dog','owner': 'ogracious'}
climy = {'kinda_animal': 'monkey','owner': 'ewurama'}
quii = {'kinda_animal': 'pig','owner': 'papa'}
pussy = {'kinda_animal': 'cat','owner': 'stein'}

pets = [biggy, climy, quii, pussy]
for pet in pets:
    if pet is biggy:
        print(pet['owner'].title() + " has a " +
        pet['kinda_animal'].title() + " as a pet.")

    elif pet is climy:
        print(pet['owner'].title() + " has a " +
        pet['kinda_animal'].title() + " as a pet.")
    
    elif pet is quii:
        print(pet['owner'].title() + " has a " +
        pet['kinda_animal'].title() + " as a pet.")
    
    else:
        print(pet['owner'].title() + " has a " +
        pet['kinda_animal'].title() + " as a pet.")
    
print("   ")

##############################################################
# Other Approach: Smart Way
biggy = {'kinda_animal': 'dog','owner': 'ogracious'}
climy = {'kinda_animal': 'monkey','owner': 'ewurama'}
quii = {'kinda_animal': 'pig','owner': 'papa'}
pussy = {'kinda_animal': 'cat','owner': 'stein'}

pets = [biggy, climy, quii, pussy]
for pet in pets:
    if pet is biggy:
        'owner' == 'ogracious'
    elif pet is climy:
        'owner' == 'ewurama'
    elif pet is quii:
        'owner' == 'papa'
    else:
        'owner' == 'ogracious'

    print(pet['owner'].title() + " has a " +
        (pet['kinda_animal'].title()) + " as a pet.")

        
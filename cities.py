cities = {
    'accra': {
        'country': 'ghana',
        'population': 30,
        'fact': 'peaceful country'
    },
    'yamousoukro': {
        'country': 'ivory coast',
        'population': 40,
        'fact': 'best producers of coffee'
    },
    'dakar': {
        'country': 'senegal',
        'population': 50,
        'fact': 'french speaking country'
    }
    }
for city, information in cities.items():
    print("\n\nCountry Name: " + information['country'].title() + "\n")
    if city is 'accra':
        print("\tThey are the most " + information['fact'] + " in Africa.")

    elif city is 'yamousoukro':
        print("\tThey are the " + information['fact'] + " in Africa.")

    else:
        print("\tSenegal is a " + information['fact'] + " in Africa.")
    
    print("\tThe capital of " + information['country'].title() + " is " + 
        city.title())
    print("\t" + information['country'].title() + " has a population of " + 
    str(information['population']) + " million.")
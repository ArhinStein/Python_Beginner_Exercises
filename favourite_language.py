from collections import OrderedDict

favourite_language = OrderedDict()

favorite_languages = {
    'jen' : 'Python',
    'sarah' : 'C',
    'edward' : 'Ruby on Rails',
    'phil' : 'Python'
    }

for name, language in favorite_languages.items():
    print(name.title() + " 's favourite language is " + language.title() + ".")
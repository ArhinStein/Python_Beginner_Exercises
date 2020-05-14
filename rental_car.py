rent_car = input("What kind of car do you like? ")
if rent_car == 'subaru':
    print("\nLet me see if I can find you a " + rent_car.title() + "!")
else:
    print("\nSorry! We don't have " + rent_car.title() + " here!.")
    
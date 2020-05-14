#Make a class called Restaurant
class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("\nThe " + self.restaurant_name.title() + " restaurant is magnificent.")
        print(self.restaurant_name.title() + " is centuries old.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " with its " + self.cuisine_type.title() + " cuisine is opened.")
    
    

class IceCreamStand(Restaurant):
    """We add attributes which stores different flavors."""
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors()
   
    def displayflavors(self, flavor):
        self.flavors = []
        for flavor in self.flavors:
            current_flavors = self.flavors.append(flavor)
        print("\nThese are the flavors we have:\n " + current_flavors)
    
nearest_restaurant = IceCreamStand('protea', 'french')
nearest_restaurant.describe_restaurant()
nearest_restaurant.open_restaurant()

restaurant = IceCreamStand('star', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

latest_restaurant = IceCreamStand('ahenfie', 'spanish')
latest_restaurant.describe_restaurant()
latest_restaurant.open_restaurant()

flavors_available = IceCreamStand()
flavors_available.displayflavors('choco', 'banana', 'apple')
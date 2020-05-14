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

nearest_restaurant = Restaurant('protea', 'french')
nearest_restaurant.describe_restaurant()
nearest_restaurant.open_restaurant()

restaurant = Restaurant('star', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

latest_restaurant = Restaurant('ahenfie', 'spanish')
latest_restaurant.describe_restaurant()
latest_restaurant.open_restaurant()
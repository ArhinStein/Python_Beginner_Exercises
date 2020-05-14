restaurant_seating = input("How many people are in your dinner group? ")
restaurant_seating = int(restaurant_seating)
if restaurant_seating > 8:
    print("\nThey will have to wait for a table!")
else:
    print("\nTable is ready!")
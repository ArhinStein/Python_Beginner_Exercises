# Make a list of sandwich orders,
# and an empty list to hold finished sandwich orders.
sandwich_orders = ['pastrami','pastrami','pastrami', 'tuna', 'peproni', 'florna', 'cheese', 'butter']

# Remove sandwich orders which are not available
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\nDeli has ran outta Pastrami Sandwich.\n ")
finished_orders = []

# Loop through sandwich orders.
# Move ordered sandwich to finished_sandwich.
while sandwich_orders:
    made_order = sandwich_orders.pop()
    print("I made your " + made_order.title() + " Sandwich!")
    finished_orders.append(made_order)

# Display all finished orders.
print("\nSandwich orders made today: ")
for finished_order in finished_orders:
    print("\t\t\t" + finished_order.title() + " Sandwich")
    
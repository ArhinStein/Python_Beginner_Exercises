# Counting
curent_number = 1
while curent_number <= 10:
    print(curent_number)
    curent_number += 1

# Quitting Message
prompt = "\nTell me something, and I will repeat back to you. "
prompt += "\n\tEnter 'quit' to  end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using 'flag' for multiple conditions
prompt = "\nTell me something, and I will repeat back to you. "
prompt += "\n\tEnter 'quit' to  end the program: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Use 'While True' to run a forever loop and use 'break' to end the statement
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

############################################################
############################################################
#Moving Items from One List to Another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# Example on Parrot
message = input("Tell me somethng, and I will repeat it back to you: ")
print(message)

# Whe your prompt is too long, make a variable and pass that variable to the input
prompt = "If you tell us who you are, we can personalize the messages you see. "
prompt += "\nWhat is your first name? "
name  = input(prompt)
print("\nHello, " + name + "!" )

# Numeriacal Input
age = input("How old are you? ")
age = int(age)
print(age)

# Modulo Operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even. ")
else: 
    print("\nThe number " + str(number) + " is odd. ")


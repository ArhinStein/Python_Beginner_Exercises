prompt = "Enter a pizza topping. "
prompt += "\nEnter 'quit' to stop: "

message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("\nI'll add " + message.title() +
        " topping to your pizza!" + "\n")    

##################################
'''
prompt = "Enter a pizza topping. "
prompt += "\nEnter 'quit' to stop: "

message = ""
while message != 'quit':
    message = input(prompt)
    print("\nI'll add " + message.title() +
        " topping to your pizza! + "\n"")    

##################################

prompt = "\nEnter a pizza topping. "
prompt += "\nEnter 'quit' to stop: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("\nI'll add " + message.title() +
        " topping to your pizza!" + "\n")    
'''
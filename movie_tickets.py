prompt = "\nEnter your age: "
message = ""
while True:
    message = input(prompt)
    message = int(message)
    if message < 3:
        print("\nThe ticket is free! ")
        break
    elif 3 <= message <= 12:
        print("\nThe ticket is $10!")   
        break 
    else:
        print("\nThe ticket is $15!")
        break
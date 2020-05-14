#Exceptions are handled using the 'try-except' block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide be zero!")

#Let's write a proper code
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    
    else:
        print(answer)

#Let's try and store the answers into "programming.txt"
filename = 'programming.txt'

with open(filename, 'w') as answer_store:
        answer_store.write(answer)
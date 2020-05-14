# Concatenation
#upper() is a method to execute the variable "name"
name = "What is your name?"
message = "Hello," + name.upper() + "!"
print(message)
n = input("what is your name?")

#New Lines/Sentences
#\n is used to start a new line while \t is for a tab
print("Language:\tPython\tC\tJava")
print("Language:\nPython\nC\nJava")
print("Language:\n\tPython\n\tC\n\tJava")

#EXAMPLE_01
#Use apostrophes ('') for a quotation
famous_person = "Albert Einstein"
person_message = '"A person who never made a\nmistake never tried anything new."'
message = famous_person + " " + "once said," + person_message
print(message)

#EXAMPLE_02
#Use str to activate an int a string 
age = 26
message_1 = "Today is my " + str(age) + "th birthday !"
print(message_1)



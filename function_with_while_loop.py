# Using an infinite loop
def get_formatted_name(first_name, last_name, m_name):
    full_name = first_name + ' ' + last_name + ' ' + m_name
    return full_name.title()
while True:
    print("Please tell me your name. ")
    print("\n(Enter 'q' to stop.) ")
    
    f_name = input("First name: ")
    l_name = input("Last name: ")
    m_name = input("Middle name: ")
    
    if f_name or l_name or m_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name, m_name)
print("\nHello " + formatted_name + "!")
import random

def generate_password():
    #string of possible characters
    chars = '1234567890'

    #empty string for the password
    password = ''

    #length of the password
    length = 16

    #generate random characters and add them to the password
    for c in range(length):
        password += random.choice(chars)

    return password

#call the function
print(generate_password())
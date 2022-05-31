# Lets import necessary libs
import random
import string

# Create function for password generation
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    print("Random string password is:", password)

# Ask user how long they want their password to be
print("\n\n")
x = int(input("Input first passwd gen length: "))
y = int(input("Input second passwd gen length: "))
z = int(input("Input third passwd gen length: "))
o = int(input("Input fourth passwd gen length: "))
print("\n")
get_random_password_string(x) # Print out the first generated password
get_random_password_string(y) # Print out the second generated password
get_random_password_string(z) # Print out the third generated password
get_random_password_string(o) # Print out the fourth generated password
print("\n\n")

# Stay tuned for version 3...

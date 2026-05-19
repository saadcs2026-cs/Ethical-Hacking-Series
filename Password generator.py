Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter password length: "))
print(f"Your password: {generate_password(length)}")

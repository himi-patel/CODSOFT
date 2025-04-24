import random

try:
    length=int(input("enter the length of the password="))

except ValueError:
    print("Invalid input. please enter a number.")
    

password_string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password_digits="0123456789"
password_special_characters="!@#$%^&*()_+[]{}|;:,.<>?/~`"

all_characters = password_string + password_digits + password_special_characters

password = ""

for i in range(length):
   password+=random.choice(all_characters)

print("your password is:",password)
import random
import string
length = int(input("Enter password length: "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
all_characters = letters + digits + symbols
password = ""
for i in range(length):
    password += random.choice(all_characters)
print("Generated Password:", password)

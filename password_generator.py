#The below will prints a strongest password_list to the user by their opinion.
import random

letters =  ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z', 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']

numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']

symbols = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')']

print("Welcome to the PyPassword Genertor...! \n You Can Generate A Strong Password From it !")

user_letters = int(input("How many 'Letters' would you like in your Password?...\n"))
user_numbers = int(input("How many 'Numbers' would you like in your Password?...\n"))
user_symbols = int(input("How many 'Symbols' would you like in your Password?...\n"))

#Easzy level

# password_list = ""

# for char in range(1 , user_letters + 1):
#     password_list += random.choice(letters)

# for char in range(1 , user_numbers + 1):
#     password_list += random.choice(numbers)

# for char in range(1 , user_symbols + 1):
#     password_list += random.choice(symbols)

# print(password_list)

#Hard level

password_list = []

for char in range(1 , user_letters + 1):
    password_list += random.choice(letters)

for char in range(1 , user_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1 , user_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")




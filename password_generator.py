import  random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
pg_letters = int(input("How many letters you would like to have in your password, give us a count?\n"))
pg_numbers = int(input ("How many numbers you would like to have in your password, give us a count?\n"))
pg_symbols = int(input("How many special characters you would like to have it in your password, give us a number?\n"))

password_list = []

for count in range(0,pg_letters):
    password_list += random.choice(letters)

for count in range(0, pg_numbers):
    password_list += random.choice(numbers)

for count in range(0,pg_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f" Your password is {password}")
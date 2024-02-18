#Password Generator Project
import random
#import pypassword
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#password = " "    
#This syntax is commonly used when initializing variables, especially when you plan to later assign a value to the variable based on some condition or user input
#print 4 character from nr_letters
# for char in range(1, nr_letters + 1):
#     #1-4 characters
#     random_char = random.choice(letters)
#     password += random_char
#     print(password)
    #random_char is a new variable and random.choice is, it returns a randomly selected item from that sequence
    #print(random_char)  #it gives letters in a bullet format
#print(random_char) # it gives only last value from random.choice value    

#password comes in sequence i.e letterssymbolsnumbers
# for char in range(1, nr_letters + 1):  #nr_letters = how much letters should we print from "letters" variable
#     password += random.choice(letters) #password = password + random.choice(letters)

# for char in range(1, nr_symbols + 1):  #nr_symbols = how much symbols should we print from "symbols" variable
#     password += random.choice(symbols)    

# for char in range (1, nr_numbers + 1):  #nr_numbers = how much numbers should we print from "numbers" variable
#     password += random.choice(numbers)

# print(password)


#password comes in shuffle format
password_list = []   #commonly used for initializing list
password = " "  #commonly used for initializing variable
#"for char in range()" means we need a characters in the range (start, end) or range(start, end, difference bet. two values)
for char in range(1, nr_letters + 1):  #nr_letters = how much letters should we print from "letters" variable
    password_list += random.choice(letters) #password_list = password_list + random.choice(letters)
# select any random letter from letters variable and put it into password_list variable.
for char in range(1, nr_symbols + 1):  #nr_symbols = how much symbols should we print from "symbols" variable
    password_list += random.choice(symbols)    
# select any random symbol from symbols variable and put it into password_list variable.
for char in range (1, nr_numbers + 1):  #nr_numbers = how much numbers should we print from "numbers" variable
    password_list += random.choice(numbers)
# select any random number from numbers variable and put it into password_list variable.
print(password_list)
random.shuffle(password_list) # shuffle variables(i.e. letters,numbers,symbols) from password_list list
print(password_list) #output comes with parenthesis"()"

# Loop through each character in the password_list
for char in password_list:
    password += char # Concatenate each character to the password string
print(f"Your password is = {password}")    #output comes without parenthesis"()"
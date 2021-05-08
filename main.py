import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = ""
random_symbols = ""
random_numbers = ""
for n in range(1,nr_letters+1):
  random_letters += letters[random.randint(0,25)]
for n in range(1,nr_symbols+1):
  random_symbols += numbers[random.randint(0,9)]
for n in range(1,nr_numbers+1):
  random_numbers += symbols[random.randint(0,8)]
result = random_letters + random_symbols + random_numbers

aux_list = []
for n in range(0,len(result)):
  aux_list.append(result[n])
random.shuffle(aux_list)

password = ""
for char in aux_list:
  password += char
print(f"Your generated password is: {password}")

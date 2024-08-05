import random
def passwordGenerator():
    lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '{', '}', '[', ']', '|', '\\', ':', ';', "'", '"', '<', '>', ',', '.', 
    '/', '?', '~', '`'
]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password=random.choice(upper_char)+random.choice(lower_char)+random.choice(special_char)+random.choice(numbers)
    password=password+password+password+password
    return password 
print(passwordGenerator())
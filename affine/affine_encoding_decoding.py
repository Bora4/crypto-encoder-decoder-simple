import os
import random
import math

def inverse_modulo(a):
    i = 1
    while True:
        if (a * i) % 26 == 1:
            return i
        else:
            i += 1

def generate_coprime_a():
    while True:
        a = random.randint(1, 25)
        if math.gcd(a, 26) == 1:
            return a

m = 26
a = generate_coprime_a()
b = random.randint(0,25)
inverse = inverse_modulo(a)

current_dir = os.path.dirname(__file__) 
# Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")
key_for_debugging = os.path.join(current_dir, "./key_for_debugging.txt")

debug_file = open(key_for_debugging, 'w+', encoding='utf-8') 
# Create or open keys_for_debugging.txt
debug_file.write(str(inverse) + "," + str(b))
# Write the keys for debugging purposes
debug_file.close()
# Close the file

with open(input_path, 'r', encoding='utf-8') as input_file:
    # Read the input file and assign it to a variable
    input_text = input_file.read()
input_file.close()

# Initialize the cyphered text
cyphered_text = "" 

# Encrypt
# Start a for loop to encrypt the text char by char
for char in input_text: 
    # Skips symbols like comma or dots
    if char.isalpha(): 
        # Check if the char is upper case
        is_upper = char.isupper() 
        
        # Normalize the chars by subtracting the unicode value 
        # of 'A' or 'a' from the char, making A or a is at 
        # position 0, B or b is at position 1 and so on.
        offset = ord('A') if is_upper else ord('a') 
        x = ord(char) - offset

        # Modular arithmetics to get the unicode value of the cyphered char
        cyphered_char = (a * x + b) % m

        # Add offset back to the unicode value of the char and cast it back to char
        cyphered_text += chr(cyphered_char + offset)
    else:
        cyphered_text += char # Append the symbol back to the text without cyphering

cypher_path = os.path.join(current_dir, "./cyphered_message.txt")


# Create or open cyphered_message.txt
cyphered_file = open(cypher_path, 'w+', encoding='utf-8') 
# Write the cyphered text
cyphered_file.write(cyphered_text) 
# Close the file
cyphered_file.close() 

# Decrypt

with open(cypher_path, 'r', encoding='utf-8') as cyphered_message_file: 
    # Read the cyphered_message file and assign it to a variable
    cyphered_text = cyphered_message_file.read()

decyphered_message = ""

# Start a for loop to decrypt the text char by char
for char in cyphered_text: 
    # Skips symbols like comma or dots
    if char.isalpha(): 

        # Check if the char is upper case
        is_upper = char.isupper() 
        
        # Normalize the chars by subtracting the unicode value of
        # 'A' or 'a' from the char, making A or a is at
        # position 0, B or b is at position 1 and so on.
        offset = ord('A') if is_upper else ord('a')
        y = ord(char) - offset

        # Decrypt using the formula: D(y) = a_inv * (y - b) % m
        decrypted_char = (inverse * (y - b)) % m

        # Add offset back to the unicode value of the char and cast it back to char
        decyphered_message += chr(decrypted_char + offset)
    else:

        # Append the symbol back to the text without cyphering
        decyphered_message += char

output_file_path = os.path.join(current_dir, "./output.txt")

# Create or open output.txt
output_file = open(output_file_path, 'w+', encoding='utf-8')
# Write the output text
output_file.write(decyphered_message)
# Close the file
output_file.close()

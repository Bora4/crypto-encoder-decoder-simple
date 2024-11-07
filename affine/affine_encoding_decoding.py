import os
import random
import math

def inverse_modulo(a):
    i = 2
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
b = random.randint(1,25)
inverse = inverse_modulo(a)

current_dir = os.path.dirname(__file__) # Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")
key_for_debugging = os.path.join(current_dir, "./key_for_debugging.txt")

debug_file = open(key_for_debugging, 'w+', encoding='utf-8') # Create or open keys_for_debugging.txt
debug_file.write(str(inverse) + "," + str(b)) # Write the keys for debugging purposes
debug_file.close() # Close the file

with open(input_path, 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()
input_file.close()

cyphered_text = "" # Initialize the cyphered text

# Encrypt
for char in input_text: # Start a for loop to encrypt the text char by char
    if char.isalpha(): # Skips symbols like comma or dots

        is_upper = char.isupper() # Check if the char is upper case
        
        # Normalize the chars by subtracting the unicode value of 'A' or 'a' from the char, making A or a is at position 0, B or b is at position 1 and so on.
        offset = ord('A') if is_upper else ord('a') 
        x = ord(char) - offset

        cyphered_char = (a * x + b) % m # Modular arithmetics to get the unicode value of the cyphered char

        cyphered_text += chr(cyphered_char + offset) # Add offset back to the unicode value of the char and cast it back to char
    else:

        cyphered_text += char # Append the symbol back to the text without cyphering

cypher_path = os.path.join(current_dir, "./cyphered_message.txt")


cyphered_file = open(cypher_path, 'w+', encoding='utf-8') # Create or open cyphered_message.txt
cyphered_file.write(cyphered_text) # Write the cyphered text
cyphered_file.close() # Close the file

# Decrypt

with open(cypher_path, 'r', encoding='utf-8') as cyphered_message_file: # Read the cyphered_message file and assign it to a variable
    cyphered_text = cyphered_message_file.read()

decyphered_message = ""

for char in cyphered_text: # Start a for loop to decrypt the text char by char
    if char.isalpha(): # Skips symbols like comma or dots

        is_upper = char.isupper() # Check if the char is upper case
        
        # Normalize the chars by subtracting the unicode value of 'A' or 'a' from the char, making A or a is at position 0, B or b is at position 1 and so on.
        offset = ord('A') if is_upper else ord('a')
        y = ord(char) - offset

        # Decrypt using the formula: D(y) = a_inv * (y - b) % m
        decrypted_char = (inverse * (y - b)) % m

        decyphered_message += chr(decrypted_char + offset) # Add offset back to the unicode value of the char and cast it back to char
    else:

        decyphered_message += char # Append the symbol back to the text without cyphering

output_file_path = os.path.join(current_dir, "./output.txt")

output_file = open(output_file_path, 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(decyphered_message) # Write the output text
output_file.close() # Close the file

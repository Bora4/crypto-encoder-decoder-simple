import os
import random
import math

def inverse_modulo(a):
    i = 1
    while True:
        if (a * i) % 29 == 1:
            return i
        else:
            i += 1

def generate_coprime_a():
    while True:
        a = random.randint(1, 28)
        if math.gcd(a, 29) == 1:
            return a

turkish_alphabet = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
m = 29
a = generate_coprime_a()
b = random.randint(0,28)
inverse = inverse_modulo(a)
current_dir = os.path.dirname(__file__) 
# Get the directory of the script
input_path = os.path.join(current_dir, "../turkish_message.txt")
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
    if char in turkish_alphabet: 
        x = turkish_alphabet.index(char)
        # Modular arithmetics to get the unicode value of the cyphered char
        cyphered_char = (a * x + b) % m
        cyphered_text += turkish_alphabet[cyphered_char]
    else:
        cyphered_text += char # Append the symbol back to the text without cyphering
cypher_path = os.path.join(current_dir, "./turkish_cyphered_message.txt")
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
    if char in turkish_alphabet: 
        y = turkish_alphabet.index(char)
        decrypted_char = (inverse * (y - b)) % m
        decyphered_message += turkish_alphabet[decrypted_char]
    else:
        # Append the symbol back to the text without cyphering
        decyphered_message += char
output_file_path = os.path.join(current_dir, "./turkish_output.txt")
# Create or open output.txt
output_file = open(output_file_path, 'w+', encoding='utf-8')
# Write the output text
output_file.write(decyphered_message)
# Close the file
output_file.close()

import random
from tr import tr

s = "abcdefghijklmnopqrstuvwxyz" # English alphabet
key = random.sample(s, len(s)) # Scramble the alphabet

with open('./input.txt', 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()

# Encryption

encrypted_text = tr(s, key, input_text) # Change the letters in the text. It changes the letter in input_text with it's correspondence in key

output_file = open('./monoalphabetic/crypted_message.txt', 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(encrypted_text) # Write the output text
output_file.close() # Close the file

# Decryption

with open('./monoalphabetic/crypted_message.txt', 'r', encoding='utf-8') as crypted_file: # Read the input file and assign it to a variable
    crypted_message = crypted_file.read()

decrypted_text = tr(key, s, crypted_message) # Decrypt the text by changing the letters of crypted_message with it's correspondence in s

output_file = open('./monoalphabetic/output.txt', 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(decrypted_text) # Write the output text
output_file.close() # Close the file
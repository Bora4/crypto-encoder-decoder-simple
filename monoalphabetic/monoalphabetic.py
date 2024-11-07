import random
from tr import tr
import os


s = "abcdefghijklmnopqrstuvwxyz" # English alphabet
key = random.sample(s, len(s)) # Scramble the alphabet

# Construct the file path dynamically
current_dir = os.path.dirname(__file__) # Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")

with open(input_path, 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()

# Encryption

encrypted_text = tr(s, key, input_text) # Change the letters in the text. It changes the letter in input_text with it's correspondence in key

crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")

output_file = open(crypted_message_path, 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(encrypted_text) # Write the output text
output_file.close() # Close the file

# Decryption


with open(crypted_message_path, 'r', encoding='utf-8') as crypted_file: # Read the input file and assign it to a variable
    crypted_message = crypted_file.read()

decrypted_text = tr(key, s, crypted_message) # Decrypt the text by changing the letters of crypted_message with it's correspondence in s

output_path = os.path.join(current_dir, "./output.txt")

output_file = open(output_path, 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(decrypted_text) # Write the output text
output_file.close() # Close the file
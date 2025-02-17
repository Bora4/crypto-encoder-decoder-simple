import random
from tr import tr
import os
# English alphabet
s = "abcdefghijklmnopqrstuvwxyz"
# Scramble the alphabet
key = random.sample(s, len(s))
# Construct the file path dynamically
current_dir = os.path.dirname(__file__) # Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")
# Read the input file and assign it to a variable
with open(input_path, 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()
# Encryption
# Change the letters in the text. It changes the letter in input_text with it's correspondence in key
encrypted_text = tr(s, key, input_text)
crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")
# Create or open crypted_message.txt
output_file = open(crypted_message_path, 'w+', encoding='utf-8')
# Write the output text
output_file.write(encrypted_text)
# Close the file
output_file.close()
# Decryption
# Read the input file and assign it to a variable
with open(crypted_message_path, 'r', encoding='utf-8') as crypted_file:
    crypted_message = crypted_file.read()
# Decrypt the text by changing the letters of crypted_message with it's correspondence in s
decrypted_text = tr(key, s, crypted_message)
output_path = os.path.join(current_dir, "./output.txt")
# Create or open output.txt
output_file = open(output_path, 'w+', encoding='utf-8')
# Write the output text
output_file.write(decrypted_text)
# Close the file
output_file.close()
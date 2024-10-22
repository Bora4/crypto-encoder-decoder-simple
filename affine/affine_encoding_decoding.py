a, b = 5, 12 # Define the key
m = 26 # Define the length of the alphabet

with open('./input.txt', 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()

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

cyphered_file = open('./affine/cyphered_message.txt', 'w+', encoding='utf-8') # Create or open cyphered_message.txt
cyphered_file.write(cyphered_text) # Write the cyphered text
cyphered_file.close() # Close the file

# Decrypt

# Modular inverse of a (5) modulo 26 is 21. This is needed to decrypt the text
a_inv = 21

with open('./affine/cyphered_message.txt', 'r', encoding='utf-8') as cyphered_message_file: # Read the cyphered_message file and assign it to a variable
    cyphered_text = cyphered_message_file.read()

decyphered_message = ""

for char in cyphered_text: # Start a for loop to decrypt the text char by char
    if char.isalpha(): # Skips symbols like comma or dots

        is_upper = char.isupper() # Check if the char is upper case
        
        # Normalize the chars by subtracting the unicode value of 'A' or 'a' from the char, making A or a is at position 0, B or b is at position 1 and so on.
        offset = ord('A') if is_upper else ord('a')
        y = ord(char) - offset

        # Decrypt using the formula: D(y) = a_inv * (y - b) % m
        decrypted_char = (a_inv * (y - b)) % m

        decyphered_message += chr(decrypted_char + offset) # Add offset back to the unicode value of the char and cast it back to char
    else:

        decyphered_message += char # Append the symbol back to the text without cyphering

output_file = open('./affine/output.txt', 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(decyphered_message) # Write the output text
output_file.close() # Close the file

import os
m = 26 # Length of the alphabet

current_dir = os.path.dirname(__file__) # Get the directory of the script
cyphered_message_path = os.path.join(current_dir, "./cyphered_message.txt")
debug_key_path = os.path.join(current_dir, "./key_for_debugging.txt")

with open(cyphered_message_path, 'r', encoding='utf-8') as cyphered_file: # Read the cyphered file and assign it to a variable
    cyphered_text = cyphered_file.read()
with open(debug_key_path, 'r', encoding='utf-8') as debug_file: # Read the cyphered file and assign it to a variable
    debug_key = debug_file.read()

decyphered_message = "Go to " + debug_key + " for the correct result \n"

for a_inv in range(1,25): # Start trying every single a value
    for b in range(1,25): # Try every b value with every a_inv value
        decyphered_message += "\nDecrypted message using " + str(a_inv) + "," + str(b) + ":\n"
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
        decyphered_message += "\n"

results_path = os.path.join(current_dir, "./brute_force_results.txt")
output_file = open(results_path, 'w+', encoding='utf-8')
output_file.write(decyphered_message) # Write the output text
output_file.close() # Close the file
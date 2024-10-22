# Go to 21,12 to see the correct result
m = 26 # Length of the alphabet
with open('./affine/cyphered_message.txt', 'r', encoding='utf-8') as cyphered_file: # Read the cyphered file and assign it to a variable
    cyphered_text = cyphered_file.read()

decyphered_message = "Go to 21,12 for the correct result \n"

for a_inv in range(0,26): # Start trying every single a value
    for b in range(0,26): # Try every b value with every a_inv value
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

output_file = open('./affine/brute_force_results.txt', 'w+', encoding='utf-8')
output_file.write(decyphered_message) # Write the output text
output_file.close() # Close the file
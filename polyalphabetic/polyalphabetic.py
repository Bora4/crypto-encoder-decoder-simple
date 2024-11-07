import os

current_dir = os.path.dirname(__file__) # Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")

with open(input_path, 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()
input_file.close()

key = "KOUATLY" # TODO: make key random
#TODO: look at slides and change this
def keygen(key, message):
    key = list(key)
    if len(message) == len(key):
        return ''.join(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encrypt(key, message: str):
    key = keygen(key, message)
    encrypted_text = []
    
    for i in range(len(message)):
        if message[i].isalpha():  # Encrypt chars only
            shift = ord(key[i].upper()) - ord('A')
            if message[i].isupper():
                encrypted_text.append(chr((ord(message[i]) + shift - ord('A')) % 26 + ord('A')))
            else:
                encrypted_text.append(chr((ord(message[i]) + shift - ord('a')) % 26 + ord('a')))
        else:
            encrypted_text.append(message[i])
            
    return ''.join(encrypted_text)

def decrypt(key, encrypted_text: str):
    key = keygen(key, encrypted_text)
    decrypted_text = []
    
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            if encrypted_text[i].isupper():
                decrypted_text.append(chr((ord(encrypted_text[i]) - shift - ord('A')) % 26 + ord('A')))
            else:
                decrypted_text.append(chr((ord(encrypted_text[i]) - shift - ord('a')) % 26 + ord('a')))
        else:
            decrypted_text.append(encrypted_text[i])
            
    return ''.join(decrypted_text)

encrypted_text = encrypt(key, input_text)

crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")

output_file = open(crypted_message_path, 'w+', encoding='utf-8') # Create or open crypted_message.txt
output_file.write(encrypted_text) # Write the crypted text
output_file.close() # Close the file

decrypted_text = decrypt(key, encrypted_text)

output_path = os.path.join(current_dir, "./output.txt")

output_file = open(output_path, 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(decrypted_text) # Write the output text
output_file.close() # Close the file
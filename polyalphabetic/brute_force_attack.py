import itertools
import string
import os
current_dir = os.path.dirname(__file__) # Get the directory of the script
crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")
with open(crypted_message_path, 'r', encoding='utf-8') as crypted_file: # Read the crypted file and assign it to a variable
    crypted_message = crypted_file.read()
crypted_file.close()
results_path = os.path.join(current_dir, "./brute_force_results.txt")
def decrypt_vigenere(crypted_message: str, key: str):
    decrypted = []
    key_length = len(key)
    for i, char in enumerate(crypted_message):
        if char.isalpha():
            shift = (ord(key[i % key_length].lower()) - ord('a')) % 26
            decrypted_char = chr(((ord(char.lower()) - shift - ord('a')) % 26) + ord('a'))
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)
def brute_force_vigenere(crypted_message, max_key_length):
    decrypted_result = ""
    english_alphabet = string.ascii_lowercase
    for key_length in range(1, max_key_length + 1):
        for key_tuple in itertools.product(english_alphabet, repeat=key_length):
            key = ''.join(key_tuple)
            decrypted_result += decrypt_vigenere(crypted_message, key)
            decrypted_result += "\n"
    return decrypted_result
decrypted_text = brute_force_vigenere(crypted_message, 3) # normally 3 is not enough but increasing the number dramatically increases the time for the attack to finish
output_file = open(results_path, 'w+', encoding='utf-8')
output_file.write(decrypted_text) # Write the output text
output_file.close() # Close the file

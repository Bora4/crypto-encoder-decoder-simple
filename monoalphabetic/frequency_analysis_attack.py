import os
from collections import Counter
import string

# The most common letter in english are E,T,A,O and most rare ones are Z,Q,X

current_dir = os.path.dirname(__file__) # Get the directory of the script
crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")

english_frequencies = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

with open(crypted_message_path, 'r', encoding='utf-8') as crypted_file: # Read the input file and assign it to a variable
    crypted_message = crypted_file.read()

def frequency_analysis_attack(crypted_message: str):
    # Count the char frequencies
    crypted_message = crypted_message.upper()
    char_counts = Counter(c for c in crypted_message if c in string.ascii_uppercase)

    # Sort the chars
    sorted_crypted_message_chars = [letter for letter, _ in char_counts.most_common()]

    # Map the chars
    substitution_map = {}
    for i, letter in enumerate(sorted_crypted_message_chars):
        if i < len(english_frequencies):
            substitution_map[letter] = english_frequencies[i]

    # Substitute each char in the message
    output = []
    for char in crypted_message:
        if char in substitution_map:
            output.append(substitution_map[char])
        else:
            output.append(char)  # Skip symbols

    return "".join(output), substitution_map

guess, mapping = frequency_analysis_attack(crypted_message)

results_path = os.path.join(current_dir, "./freq_analysis_result.txt")
output_file = open(results_path, 'w+', encoding='utf-8')
output_file.write(guess) # Write the output text
output_file.close() # Close the file

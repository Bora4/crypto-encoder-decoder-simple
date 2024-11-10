import os
import random

S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

INITIAL_PERMUTATION_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

PERMUTATION_TABLE = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

FINAL_PERMUTATION_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute(input_text, table):
    return [input_text[i - 1] for i in table]

def shift_left(bits, num_shifts):
    return bits[num_shifts:] + bits[:num_shifts]

def generate_round_keys(key):
    key56 = permute(key, PC1)
    round_keys = []
    combined_key = key56
    for i in range(16):
        left, right = combined_key[:28], combined_key[28:]
        left = shift_left(left, SHIFT_SCHEDULE[i])
        right = shift_left(right, SHIFT_SCHEDULE[i])
        combined_key = left + right
        round_key = permute(combined_key, PC2)
        round_keys.append(round_key)
    return round_keys

def final_permutation(input_text):
    permutated_text = (input_text[i - 1] for i in FINAL_PERMUTATION_TABLE)
    return ''.join(map(str, permutated_text))

def split(state):
    left_half = state[:32]
    right_half = state[32:]
    return left_half, right_half

def expand(right_half):
    return [right_half[i - 1] for i in EXPANSION_TABLE]

def s_box_substitution(state):
    output = []
    for i in range(8): # 8 S-boxes
        block = state[i*6:(i+1)*6]
        # binary_string = f"{block[0]:b}{block[5]:b}"
        row = int(f"{block[0]}{block[5]}", 2)
        # row = int(binary_string, 2)
        col = int("".join(map(str, block[1:5])), 2)
        # binary_string = f"{block[1]:b}{block[5]:b}"
        # col = int(binary_string, 2)
        value = S_BOXES[i][row][col]
        output += [int(bit) for bit in f"{value:04b}"]
    return output

def xor(bits1, bits2):
    return [int(b1) ^ int(b2) for b1, b2 in zip(bits1, bits2)]

def round_of_encryption(left_half, right_half, round_key):

    expanded = expand(right_half) # E(R_0) (48 bits)
    xored = xor(expanded, round_key)  # K_1+E(R_0) (48 bits)
    substituted = s_box_substitution(xored)  # S_1(B_1)...S_8(B_8) (32 bits)
    permuted = permute(substituted, PERMUTATION_TABLE)  # f (32 bits)
    new_left_half = right_half  # New left half is the old right half
    new_right_half = xor(permuted, left_half)  # XOR with the left half
    return new_left_half, new_right_half

def des_encryption(input_text, key):
    # Steps:
    ## Add padding if the message length is not 0 modulo 64
    ## Inital Permutation
    ## Splitting left and right halves
    ## 16 rounds of encryption
    ## Final Swap
    ## Final Permutation

    binary_string = ''.join(f"{ord(char):08b}" for char in input_text)
    # Padding
    if len(binary_string) % 64 != 0:
        padding_length = 64 - (len(binary_string) % 64)
        padding_byte = format(padding_length, '08b')
        padding = padding_byte * int((padding_length/8))
        binary_string += padding

    blocks = [[int(bit) for bit in binary_string[i:i+64]] for i in range(0, len(binary_string), 64)]
    encrypted_blocks = ''
    round_keys = generate_round_keys(key)
    for block in blocks:
        state = permute(block, INITIAL_PERMUTATION_TABLE)
        state_left_half, state_right_half = split(state)
        # Apply 16 rounds of encryption
        for i in range(16):
            state_left_half, state_right_half = round_of_encryption(state_left_half, state_right_half, round_keys[i])
        combined_block = state_right_half + state_left_half  # Combine right and left halves
        final_output = final_permutation(combined_block)  # Apply final permutation
        encrypted_blocks += final_output
    return encrypted_blocks

current_dir = os.path.dirname(__file__) # Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")

with open(input_path, 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()
input_file.close()

key = format(random.getrandbits(64), '064b') # Generate random key
encrypted_text = des_encryption(input_text, key) # Start encryption

crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")
crypted_file = open(crypted_message_path, 'w+', encoding='utf-8') # Create or open crypted_message.txt
crypted_file.write(encrypted_text) # Write the ciphertext
crypted_file.close() # Close the file

def des_decrypt(ciphertext, key):
    # Decryption is the same operation as encryption using the keys in reverse order
    # Steps:
    ## Key generation
    ## Inital Permutation
    ## Splitting left and right halves
    ## 16 rounds of encryption
    ## Final Swap
    ## Final Permutation
    ## Remove Padding    
    
    blocks = [[int(bit) for bit in ciphertext[i:i+64]] for i in range(0, len(ciphertext), 64)]
    decrypted_blocks = ''
    round_keys = generate_round_keys(key)
    round_keys_reverse = round_keys[::-1]
    for block in blocks:
        state = permute(block, INITIAL_PERMUTATION_TABLE)
        state_left_half, state_right_half = split(state)
        for i in range(16):
            state_left_half, state_right_half = round_of_encryption(state_left_half, state_right_half, round_keys_reverse[i])
        combined_block = state_right_half + state_left_half  # Combine right and left halves
        final_output = final_permutation(combined_block)  # Apply final permutation
        decrypted_blocks += final_output
    
    padding_length = int(decrypted_blocks[-8:], 2)  # Last 8 bits as int
    expected_padding = format(padding_length, '08b') * int(padding_length / 8)

    if decrypted_blocks[-(padding_length):] == expected_padding:
        decrypted_blocks = decrypted_blocks[:-(padding_length)]
    else:
        raise ValueError("Invalid padding detected")

    return decrypted_blocks

with open(crypted_message_path, 'r', encoding='utf-8') as ciphered_message: # Read the input file and assign it to a variable
    ciphertext = ciphered_message.read()
ciphered_message.close()
message_in_bits = des_decrypt(ciphertext, key)
byte_array = [message_in_bits[i:i+8] for i in range(0, len(message_in_bits), 8)]
characters = [chr(int(byte, 2)) for byte in byte_array]
decrypted_message = ''.join(characters)

output_file_path = os.path.join(current_dir, "./output.txt")
output_file = open(output_file_path, 'w+', encoding='utf-8') # Create or open output.txt
output_file.write(decrypted_message) # Write the decrypted message
output_file.close() # Close the file

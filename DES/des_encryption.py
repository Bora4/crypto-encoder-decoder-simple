import os

S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 2, 8, 14, 3, 10, 6, 12, 11, 9, 7, 4, 1, 13, 0, 5]
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
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 2, 8, 13, 7, 4, 2],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 15, 1, 11],
        [3, 13, 4, 1, 13, 10, 6, 0, 5, 8, 15, 14, 9, 11, 2, 7],
        [9, 4, 5, 11, 2, 14, 3, 15, 1, 10, 0, 6, 7, 8, 12, 13]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        [10, 6, 9, 5, 0, 7, 1, 2, 3, 14, 15, 8, 13, 4, 12, 11],
        [1, 10, 13, 7, 2, 8, 4, 14, 9, 0, 6, 12, 11, 3, 5, 15]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 9, 5, 3, 14, 15, 0, 8, 13],
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 1, 7, 6, 13, 9, 11, 0, 14, 3, 5, 12, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 1, 7, 6, 13, 9, 11, 0, 14, 3, 5, 12, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 0, 14, 7, 9, 5, 10, 15, 1, 8, 13, 6, 11]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 1, 3, 12, 10, 15, 9, 2, 8, 0, 5, 14, 11, 4, 13, 7]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 6, 3, 11, 5]
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

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2,2, 1]

key = "1010101010111011000010101011101100001111000011110000111100001111"

def permute(input_text, table):
    
    return [input_text[i - 1] for i in table]

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
        row = int(f"{block[0]}{block[5]}", 2)
        col = int("".join(map(str, block[1:5])), 2)
        value = S_BOXES[i][row][col]
        output += [int(bit) for bit in f"{value:04b}"]
    return output

def xor(bits1, bits2):
    return [int(b1) ^ int(b2) for b1, b2 in zip(bits1, bits2)]

def generate_round_keys(key):
    key56 = permute(key, PC1) #TODO: figure out differences between PERMUTATION_TABLE AND PC

    round_keys = []

    for i in range(16):
        round_key = permute(key56, PC2)
        round_keys.append(round_key[:48])  # 48-bit round key
    return round_keys

def round_of_encryption(left_half, right_half, round_key):

    expanded = expand(right_half)
    xored = xor(expanded, round_key)  # Key mixing
    substituted = s_box_substitution(xored)  # S-box substitution
    permuted = permute(substituted, PERMUTATION_TABLE)  # Permutation P
    new_left_half = right_half  # New left half is the old right half
    new_right_half = xor(permuted, left_half)  # XOR with the left half
    return new_left_half, new_right_half

def des_encryption(input_text):
    # Steps:
    ## Inital Permutation
    ## Splitting left and right halves
    ## 16 rounds of encryption
    ## Final Swap
    ## Final Permutation
    # Pad the input to ensure its length is a multiple of 64 bits

    binary_string = ''.join(f"{ord(char):08b}" for char in input_text)

    if len(binary_string) % 64 != 0:
        padding_length = 64 - (len(binary_string) % 64)
        binary_string += '0' * padding_length

    blocks = [[int(bit) for bit in binary_string[i:i+64]] for i in range(0, len(binary_string), 64)]
    
    encrypted_blocks = ''

    for block in blocks:
        print(block)
        round_keys = generate_round_keys(key)

        state = permute(block, INITIAL_PERMUTATION_TABLE)
        state_left_half, state_right_half = split(state)

        for i in range(16):
            state_left_half, state_right_half = round_of_encryption(state_left_half, state_right_half, round_keys[i])
        
        combined_block = state_left_half + state_right_half  # Combine right and left halves
        final_output = final_permutation(combined_block)  # Apply final permutation
        encrypted_blocks += final_output
    print(encrypted_blocks)
    return encrypted_blocks

current_dir = os.path.dirname(__file__) # Get the directory of the script
input_path = os.path.join(current_dir, "../input.txt")

with open(input_path, 'r', encoding='utf-8') as input_file: # Read the input file and assign it to a variable
    input_text = input_file.read()
input_file.close()

encrypted_text = des_encryption(input_text)

crypted_message_path = os.path.join(current_dir, "./crypted_message.txt")
output_file = open(crypted_message_path, 'w+', encoding='utf-8') # Create or open crypted_message.txt
output_file.write(encrypted_text) # Write the crypted text
output_file.close() # Close the file
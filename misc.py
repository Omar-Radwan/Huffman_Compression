KB_SIZE = 1024
DELIM = ','
ENCODING = "latin_1"


# def count_char_frequency(file_name: str) -> dict:
#     frequency: dict = {}
#     file = open(file_name, "r")
#     for line in file:
#         for character in line:
#             frequency[character] = frequency.get(character, 0) + 1
#     return frequency
#

def total_number_of_bits(frequency: dict, huffman_code: dict):
    total_bits_number = 0
    for character in frequency:
        character_frequency = frequency[character]
        character_code = huffman_code[character]
        total_bits_number += (character_frequency * len(character_code))
    return total_bits_number


def list_to_ascii(x: []):
    result, pow2 = 0, 1
    for i in range(len(x) - 1, -1, -1):
        result += pow2 * x[i]
        pow2 *= 2
    return result


def char_to_binary(x: str) -> str:
    """
    :param x: some character
    :return: binary representation of the input character
    """
    val = ord(x)
    return '{0:08b}'.format(val)

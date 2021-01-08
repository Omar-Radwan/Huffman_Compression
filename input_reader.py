from collections import deque
from misc import *


class InputReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "r",newline='', encoding=ENCODING)
        self.text = self.file.read()
        self.file.close()

    def read_compression_details(self, i):
        compressedCharacters, i = self.get_length(i)

        lastBitsToReadString = ""
        while self.text[i] != ",":
            lastBitsToReadString += self.text[i]
            i += 1
        lastBitsToRead = int(lastBitsToReadString)
        print(lastBitsToRead)
        return compressedCharacters, lastBitsToRead, i + 1

    def read_path(self, i):
        pathCharacters, i = self.get_length(i)

        path = ""
        while pathCharacters != 0:
            path += str(self.text[i])
            i += 1
            pathCharacters -= 1
        print(path)
        return path, i

    def read_meta_data(self, i) -> ({}, int):
        huffmanCodes = {}
        huffmanCharacters, i = self.get_length(i)

        while huffmanCharacters != 0:
            key = self.text[i]
            value = ""
            i += 1
            huffmanCharacters -= 1
            while self.text[i] != DELIM:
                value += self.text[i]
                i += 1
                huffmanCharacters -= 1
            huffmanCharacters -= 1
            huffmanCodes[value] = key
            i += 1
        print(huffmanCodes)
        return huffmanCodes, i

    def get_length(self, i):
        length_string = ""
        while self.text[i] != DELIM:
            length_string += str(self.text[i])
            i += 1
        length = int(length_string)
        i += 1
        return length, i

    def get_compressed_bits(self, i, count, last_bits):
        characters = self.text[i:i + count - 1]
        bits = []


        for character in characters:
            binary_string = char_to_binary(character)
            for bit in binary_string:
                bits.append(bit)
        # l ... r = r-l+1 = n  ... l,n -> r = l+n-1
        binary_string = char_to_binary(self.text[i + count - 1])
        for j in range(last_bits):
            bits.append(binary_string[j])
        return bits, i + count

    def close(self):
        self.file.close()
# def fill_buffer(self, is_clear=True):
#     if (is_clear):
#         self.buffer.clear()
#     read_str = self.file.read(KB_SIZE - len(self.buffer))
#     for c in read_str:
#         self.buffer.append(c)
#     return len(read_str) != 0
#
# def fill_limited_buffer(self, read_so_far, total_number_of_characters, is_clear=True):
#     if (is_clear):
#         self.buffer.clear()
#     # read_str = self.line[read_so_far:min(KB_SIZE, total_number_of_characters)]
#     read_str = self.text[read_so_far:]
#     for c in read_str:
#         for x in char_to_ascii(c):
#             self.buffer.append(x)
#     return len(read_str) != 0

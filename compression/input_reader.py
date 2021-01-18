from collections import deque
from misc.constants import *


class InputReader:
    def __init__(self, file_name):
        self.read_so_far = 0
        self.file_name = file_name
        self.file = open(self.file_name, "r", newline='', encoding=ENCODING)

    def read_compression_lengths(self):
        compressed_characters = self.get_length()
        last_bits_to_read = self.get_length()
        return compressed_characters, last_bits_to_read

    def read_whole_file(self):
        self.text = self.file.read()

    def read_path(self):
        path_characters = self.get_length()
        path = self.file.read(path_characters)
        self.read_so_far += path_characters
        return path

    def __long_value(self, value_list, compact):
        ascii_val = ord(compact)
        size = ascii_val >> 5
        for shift in range(size - 1, -1, -1):
            pow = (1 << shift) & ascii_val
            value_list.append('0') if (pow == 0) else value_list.append('1')

    def read_meta_data(self) -> ({}, int):
        huffmanCodes = {}
        huffman_characters = self.get_length()
        end = self.read_so_far + huffman_characters

        while self.read_so_far < end:
            key = self.file.read(1)
            self.read_so_far += 1
            tmp = self.file.read(1)
            value_list = []
            while tmp != DELIMITER:
                self.__long_value(value_list, tmp)
                self.read_so_far += 1
                tmp = self.file.read(1)
            value = "".join(value_list)
            huffmanCodes[value] = key
            self.read_so_far += 1
        return huffmanCodes

    def get_length(self):
        tmp = self.file.read(1)
        if tmp == '':
            return 0

        length_list = []
        while tmp != DELIMITER:
            length_list.append(tmp)
            self.read_so_far += 1
            tmp = self.file.read(1)
        self.read_so_far += 1
        length = int("".join(length_list))
        return length

    def get_compressed_bits(self, count, useful_bits_from_last_byte):
        bits = deque([])
        if count == 0:
            return  bits
        characters = self.file.read(count - 1)
        for character in characters:
            binary_string = '{0:08b}'.format(ord(character))
            for bit in binary_string:
                bits.append(bit)
        if (count >= 1):
            binary_string = '{0:08b}'.format(ord(self.file.read(1)))
            for useful_bits in range(useful_bits_from_last_byte):
                bits.append(binary_string[useful_bits])
            self.read_so_far += count

        return bits

    def close(self):
        self.file.close()

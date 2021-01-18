from collections import deque

from compression.input_reader import InputReader
from misc.constants import *


class OutputWriter:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = open(self.file_name, "w", newline='', encoding=ENCODING)
        self.text_list = []

    def write_to_file(self, character: str):
        self.text_list.append(character)
        if (len(self.text_list) >= 50 * KB_SIZE):
            self.file.write("".join(self.text_list))
            self.text_list = []

    def __compact(self, code_str: str):
        ret = []
        dq = deque([int(c) for c in code_str])
        while len(dq) > 0:
            size = min(5, len(dq))
            cur = size << 5
            for shift in range(size - 1, -1, -1):
                cur += (1 << shift) * dq.popleft()
            ret.append(chr(cur))
        return "".join(ret)

    def write_huffman_codes(self, huffman_codes: dict):
        pairs_list = []
        for key, value in huffman_codes.items():
            pairs_list.append(key + self.__compact(value) + DELIMITER)

        length = self.__huffman_codes_length(huffman_codes)
        pairs_line = str(length) + DELIMITER + "".join(pairs_list)
        self.write_to_file(pairs_line)

    def __huffman_codes_length(self, huffman_codes: dict):
        return 2 * len(huffman_codes) + sum(((len(value)+4)//5) for value in huffman_codes.values())

    def write_path(self, path: str):
        line = "".join([str(len(path)), DELIMITER, path])
        self.write_to_file(line)

    def compressed_bits_length(self, text: str, huffman_codes: dict):
        return sum(len(huffman_codes[c]) for c in text)

    def __compress_bits_to_chars(self, buffer_dq: deque):
        while len(buffer_dq) >= 8:
            ascii_code = sum(buffer_dq.popleft() * (1 << (7 - i)) for i in range(8))
            self.write_to_file(chr(ascii_code))

    def write_compressed_data(self, huffman_codes: dict, file_name: str):
        input_reader = InputReader(file_name)
        input_reader.read_whole_file()
        bits_length = self.compressed_bits_length(input_reader.text, huffman_codes)
        char_count, readable_from_last_char = bits_length // 8, bits_length % 8

        if (readable_from_last_char != 0):
            char_count += 1

        if readable_from_last_char == 0:
            readable_from_last_char = 8

        line = "".join([str(char_count), DELIMITER, str(readable_from_last_char), DELIMITER])
        self.write_to_file(line)
        input_reader.close()

        dq = deque([])

        for character in input_reader.text:
            code = huffman_codes[character]
            for bit in code:
                dq.append(int(bit))
                self.__compress_bits_to_chars(dq)

        if len(dq) > 0:
            while len(dq) != 8:
                dq.append(0)
            self.__compress_bits_to_chars(dq)
        input_reader.close()
        return char_count

    def close(self):
        self.file.write("".join(self.text_list))
        self.file.close()

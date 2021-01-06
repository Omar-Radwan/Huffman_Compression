from collections import deque

from misc import *


class OutputWriter:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.output_buffer = []

    def write_to_file(self, character: str):
        if len(self.output_buffer) < KB_SIZE:
            self.output_buffer.append(character)
        else:
            file = open(self.file_name, "w")
            file.write("".join(self.output_buffer))
            self.output_buffer.clear()
            file.close()

    def write_meta_data(self, huffman_codes: dict, frequency: dict, file_name):
        total_bits_number = total_number_of_bits(frequency, huffman_codes)
        readable_bits = total_bits_number - total_bits_number % 8

        file = open("output.txt", "w")
        file.write(str(len(huffman_codes)))

        for key, value in huffman_codes.items():
            pair = key + " " + value + "\n"
            file.write(str(pair))

        file.write(str(readable_bits))
        file.close()
        pass

    def write_compressed_data(self, huffman_codes: dict, file_name):
        buffer_dq = deque([])
        original_file = open(file_name, "r")
        compressed_file = open("output.txt", "w", encoding='utf-8')
        for line in original_file:
            for character in line:
                code = huffman_codes[character]
                for bit in code:
                    buffer_dq.append(int(bit))
                while len(buffer_dq) >= 8:
                    byte_binary = [buffer_dq.popleft() for i in range(8)]
                    ascii_code = list_to_ascii(byte_binary)
                    out_char = chr(ascii_code)
                    print(out_char)
                    compressed_file.write(out_char)
                    # TODO: write to file

        # TODO: what if deque is not empty?
        if len(buffer_dq) > 0:
            length = len(buffer_dq)
            byte_binary = [buffer_dq.popleft() for i in range(length)]
            while len(byte_binary) < 8:
                byte_binary.append('0')
                ascii_code = list_to_ascii(byte_binary)
                out_char = chr(ascii_code)
                compressed_file.write(out_char)


o = OutputWriter()
huffman_codes = {'\n': '00', 'd': '01', 's': '100', 'b': '1010', 'c': '1011', 'a': '11'}
o.write_compressed_data(huffman_codes, "input.txt")

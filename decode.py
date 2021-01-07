from input_reader import InputReader
from node import DecodeNode
from output_writer import OutputWriter
from collections import deque


class Decoder:
    def __init__(self, inpute_file_name: str, output_file_name: str):
        self.input_reader = InputReader(inpute_file_name, True)
        self.output_writer = OutputWriter(output_file_name)

    def build_decode_tree(self, huffman_codes: dict):
        self.decode_root = DecodeNode()
        for code, character in huffman_codes:
            self.__add_node_in_decode_tree(0, code, self.decode_root, character)

    def __add_node_in_decode_tree(self, pos_in_code: int, code: str, node: DecodeNode, character: str):
        if pos_in_code == len(code):
            node.character = character
            return
        if code[pos_in_code] == '0':
            node.left = DecodeNode()
            self.__add_node_in_decode_tree(pos_in_code + 1, code, node.left, character)
        else:
            node.right = DecodeNode()
            self.__add_node_in_decode_tree(pos_in_code + 1, code, node.right, character)

    def read_character(self, node: DecodeNode):
        if node.character != None:
            return node.character
        if len(self.input_reader.buffer) == 0:
            return None
        removed = deque.popleft(self.input_reader.buffer)
        result = self.read_character(node.left) if removed == '0' else self.read_character(node.right)
        if result == None:
            deque.appendleft(self.input_reader.buffer, removed)
        return result

    def decode_file(self):
        read_so_far = 0
        huffman_codes, read_so_far = self.input_reader.read_meta_data(read_so_far)
        self.build_decode_tree(huffman_codes)
        # dowhile
        path, read_so_far = self.input_reader.read_path(read_so_far)
        while len(path) > 0:
            number_of_compressed, number_of_last_bits = self.input_reader.read_compression_details(read_so_far)
            while self.input_reader.fill_limited_buffer(read_so_far, max(0, number_of_compressed)):
                character = self.read_character(self.decode_root)
                while character != None:
                    self.output_writer.write_to_file(character)
                    character = self.read_character(self.decode_root)
                number_of_compressed -= len(self.input_reader.buffer)
            path, read_so_far = self.input_reader.read_path(read_so_far)

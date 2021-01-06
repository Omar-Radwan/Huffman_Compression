from input_reader import InputReader
from node import DecodeNode
from output_writer import OutputWriter
from collections import deque


class Decoder:
    def __init__(self, inpute_file_name: str, output_file_name: str):
        self.input_reader = InputReader(inpute_file_name)
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


# A101011111010101010101010101010101010 101

def decode_file(self):
    while not self.input_reader.file_ended():
        self.input_reader.fill_buffer()
        character = self.read_character(self.decode_root)
        while character != None:
            self.output_writer.write_to_file(character)
            character = self.read_character(self.decode_root)

from input_reader import InputReader
from node import DecodeNode
from output_writer import OutputWriter
from collections import deque


class Decoder:
    def __init__(self, inpute_file_name: str):
        self.input_reader = InputReader(inpute_file_name)

    def inorder(self, node: DecodeNode):
        if not node:
            return

        self.inorder(node.left)
        if not node.left and not node.right:
            print(f'{node.character}  -->  {node.code}')
        self.inorder(node.right)

    def build_decode_tree(self, huffman_codes: dict):
        self.decode_root = DecodeNode()
        for code, character in huffman_codes.items():
            self.__add_node_in_decode_tree(0, code, self.decode_root, character)

    def __add_node_in_decode_tree(self, pos_in_code: int, code: str, node: DecodeNode, character: str):
        if pos_in_code == len(code):
            node.character = character
            node.code = code
            return
        if code[pos_in_code] == '0':
            if node.left == None:
                node.left = DecodeNode()
            self.__add_node_in_decode_tree(pos_in_code + 1, code, node.left, character)
        else:
            if node.right == None:
                node.right = DecodeNode()
            self.__add_node_in_decode_tree(pos_in_code + 1, code, node.right, character)

    def read_character(self, bits, node: DecodeNode):
        if node.character != None:
            return node.character
        return self.read_character(bits, node.left) if (bits.popleft() == '0') else self.read_character(bits,
                                                                                                        node.right)

    def decode(self):
        huffman_codes = self.input_reader.read_meta_data()
        self.build_decode_tree(huffman_codes)
        self.inorder(self.decode_root)
        path = self.input_reader.read_path()

        while len(path) > 0:
            output_writer = OutputWriter(f'{path}.decoded.txt')
            compressed_length, last_bits = self.input_reader.read_compression_lengths()

            bits = self.input_reader.get_compressed_bits(compressed_length, last_bits)

            character = self.read_character(bits, self.decode_root)
            output_writer.write_to_file(character)
            while len(bits) > 0:
                character = self.read_character(bits, self.decode_root)
                output_writer.write_to_file(character)
            output_writer.close()
            path = self.input_reader.read_path()


        self.input_reader.close()

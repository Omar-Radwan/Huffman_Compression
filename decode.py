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
            if not node.left:
                node.left = DecodeNode()
            self.__add_node_in_decode_tree(pos_in_code + 1, code, node.left, character)
        else:
            if not node.right:
                node.right = DecodeNode()
            self.__add_node_in_decode_tree(pos_in_code + 1, code, node.right, character)

    def read_character(self, i, bits, node: DecodeNode):
        if node.character != None:
            return node.character, i
        return self.read_character(i + 1, bits, node.left) if (bits[i] == '0') else self.read_character(i + 1, bits,
                                                                                                        node.right)

    def decode_file(self):
        read_so_far = 0
        huffman_codes, read_so_far = self.input_reader.read_meta_data(read_so_far)
        self.build_decode_tree(huffman_codes)
        self.inorder(self.decode_root)

        # dowhile
        path, read_so_far = self.input_reader.read_path(read_so_far)
        while len(path) > 0:
            output_writer = OutputWriter(f'dadaoda{path}')
            compressed_length, last_bits, read_so_far = self.input_reader.read_compression_details(
                read_so_far)
            bits, read_so_far = self.input_reader.get_compressed_bits(read_so_far, compressed_length, last_bits)
            index_in_bits = 0
            character, index_in_bits = self.read_character(index_in_bits, bits, self.decode_root)
            output_writer.write_to_file(character)
            while index_in_bits < len(bits):
                character, index_in_bits = self.read_character(index_in_bits, bits, self.decode_root)
                output_writer.write_to_file(character)
            output_writer.close()
            if read_so_far < len(self.input_reader.text):
                path, read_so_far = self.input_reader.read_path(read_so_far)
            else:
                path, read_so_far = "", read_so_far

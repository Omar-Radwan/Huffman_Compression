from input_reader import InputReader
from node import DecodeNode
from output_writer import OutputWriter
from collections import deque


class Decoder:
    def __init__(self, inpute_file_name: str, output_file_name: str):
        self.input_reader = InputReader(inpute_file_name, True)
        self.output_writer = OutputWriter(output_file_name)

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

    def read_character(self, node: DecodeNode):
        if node.character != None:
            return node.character
        if len(self.input_reader.buffer) == 0:
            return None
        #removed = deque.popleft(self.input_reader.buffer)
        removed = self.input_reader.buffer.popleft()
        #result = self.read_character(node.left) if removed == '0' else self.read_character(node.right)
        if removed == '0':
            result = self.read_character(node.left)
        else:
            result = self.read_character(node.right)
        if result == None:
            self.input_reader.buffer.appendleft(removed)
        return result

    def decode_file(self):
        read_so_far = 0
        huffman_codes, read_so_far = self.input_reader.read_meta_data(read_so_far)
        self.build_decode_tree(huffman_codes)
        self.inorder(self.decode_root)
        # dowhile
        path, read_so_far = self.input_reader.read_path(read_so_far)
        while len(path) > 0:
            number_of_compressed, number_of_last_bits, read_so_far= self.input_reader.read_compression_details(read_so_far)
            buffer_not_empty, read_so_far = self.input_reader.fill_limited_buffer(read_so_far, max(0, number_of_compressed))
            while buffer_not_empty:
                character = self.read_character(self.decode_root)
                while character != None:
                    self.output_writer.write_to_file(character)
                    character = self.read_character(self.decode_root)
                number_of_compressed -= len(self.input_reader.buffer)
                buffer_not_empty, read_so_far = self.input_reader.fill_limited_buffer(read_so_far, max(0, number_of_compressed))
            path, read_so_far = self.input_reader.read_path(read_so_far)
        self.output_writer.close()

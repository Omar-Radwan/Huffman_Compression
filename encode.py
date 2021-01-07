import heapq

from input_reader import InputReader
from node import HuffmanNode, DecodeNode
from output_writer import OutputWriter


class Encoder:
    def __init__(self, input_file_names, output_file_name: str):
        self.input_file_names = input_file_names
        self.output_writer = OutputWriter(output_file_name)
        self.frequency = {}
        self.huffman_codes = {}
        self.root_node = None

    def build_huffman_tree(self):
        pq = []
        for key, value in self.frequency.items():
            node = HuffmanNode(value, key)
            heapq.heappush(pq, node)

        while len(pq) != 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            sum = x.frequency + y.frequency
            z = HuffmanNode(frequency=sum, left=x, right=y)
            heapq.heappush(pq, z)

        return pq[0]

    def traverse_huffman_tree(self, node: HuffmanNode, current_code: str):
        if node == None:
            return

        if node.left == None and node.right == None:
            self.huffman_codes[node.character] = current_code

        self.traverse_huffman_tree(node.left, current_code.__add__('0'))
        self.traverse_huffman_tree(node.right, current_code.__add__('1'))

    def count_char_frequency(self, txt: str):
        for character in txt:
            self.frequency[character] = self.frequency.get(character, 0) + 1

    def encode(self):
        for file_name in self.input_file_names:
            input_reader = InputReader(file_name, False)
            while input_reader.fill_buffer():
                self.count_char_frequency(input_reader.buffer)

        if len(self.frequency) > 1:
            root_node = self.build_huffman_tree()
            self.traverse_huffman_tree(root_node, '')
        else:
            self.huffman_codes[list(self.frequency.keys())[0]] = '0'

        self.output_writer.write_meta_data(self.huffman_codes)
        for file_name in self.input_file_names:
            self.output_writer.write_path(file_name)
            self.output_writer.write_compressed_data(self.huffman_codes, file_name)
        self.output_writer.close()
        """
            Compressed File:
                1.no. of characters in huffman codes+huffman codes     
                2.no. of characters in path + path 
                3.no. of characters in compressed data|no. or bits to read from last char|compressed data
                
            any character that mustn't be added won't be added
            40                              
            number of chars to read k123 k123 k123 12 abc\\xyz\\a12 3 aksjdlkasjdlkasjdlksaalkasj        
            size of dict = n
            2n+sum(length of values)                             
        """

import heapq
import os

from compression.input_reader import InputReader
from misc.node import HuffmanNode
from compression.output_writer import OutputWriter


class Encoder:
    def __init__(self, input_path):
        if (os.path.isdir(input_path)):
            self.input_file_names = self.files_in_directory(input_path)
            self.output_writer = OutputWriter(input_path + '_compressed.txt')
        else:
            self.input_file_names = [input_path]
            self.output_writer = OutputWriter(self.modify_name(input_path))
        self.frequency = {}
        self.huffman_codes = {}
        self.root_node = None
        self.compressed_chars_count = 0

    def modify_name(self, input_path: str):
        index_of_point = input_path.rfind('.')
        if (index_of_point == -1):
            input_path = input_path + ('_compressed' + '.txt')
        else:
            input_path = input_path[0:index_of_point] + '_compressed' + input_path[index_of_point:]
        return input_path

    def files_in_directory(self, path: str):
        fname = []
        for root, directoryNames, fileNames in os.walk(path):
            for file in fileNames:
                fname.append(os.path.join(root, file))
        return fname

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

    def traverse_huffman_tree(self, node: HuffmanNode, current_code: []):
        if node == None:
            return

        if node.left == None and node.right == None:
            self.huffman_codes[node.character] = ''.join(current_code)
        current_code.append('0')
        self.traverse_huffman_tree(node.left, current_code)
        current_code.pop()
        current_code.append('1')
        self.traverse_huffman_tree(node.right, current_code)
        current_code.pop()

    def count_char_frequency(self, txt: str):
        for character in txt:
            self.frequency[character] = self.frequency.get(character, 0) + 1

    def encode(self):

        for file_name in self.input_file_names:
            input_reader = InputReader(file_name)
            input_reader.read_whole_file()
            self.count_char_frequency(input_reader.text)
            input_reader.close()

        if len(self.frequency) > 1:
            root_node = self.build_huffman_tree()
            self.traverse_huffman_tree(root_node, [])
        elif len(self.frequency) == 1:
            self.huffman_codes[list(self.frequency.keys())[0]] = '0'
        self.output_writer.write_huffman_codes(self.huffman_codes)
        for file_name in self.input_file_names:
            self.output_writer.write_path(file_name)
            self.compressed_chars_count += self.output_writer.write_compressed_data(self.huffman_codes, file_name)

        self.output_writer.close()
        return True

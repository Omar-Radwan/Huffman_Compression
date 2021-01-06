import heapq
from node import HuffmanNode, DecodeNode


class Encoder:
    def __init__(self):
        pass

    def build_huffman_codes(self, frequency: dict) -> dict:

        pq = []
        for key, value in frequency.items():
            node = HuffmanNode(value, key)
            heapq.heappush(pq, node)
        # TODO: corner case when file has only one character

        while len(pq) != 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            sum = x.frequency + y.frequency
            z = HuffmanNode(frequency=sum, left=x, right=y)
            heapq.heappush(pq, z)

        huffman_codes: dict = {}

        self.traverse_huffman_tree(pq[0], '', huffman_codes) if (len(frequency) != 1) else huffman_codes[
            list(frequency.keys())[0]] = '0'

        return huffman_codes

    def traverse_huffman_tree(self, node: HuffmanNode, current_code: str, huffman_codes: dict):
        if node == None:
            return

        if node.left == None and node.right == None:
            huffman_codes[node.character] = current_code

        self.traverse_huffman_tree(node.left, current_code.__add__('0'), huffman_codes)
        self.traverse_huffman_tree(node.right, current_code.__add__('1'), huffman_codes)

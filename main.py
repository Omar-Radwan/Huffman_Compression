import heapq

from decode import Decoder
from node import HuffmanNode, DecodeNode
from collections import deque
import ast
from output_writer import OutputWriter
from encode import Encoder

if __name__ == '__main__':
    encoder = Encoder(["input.txt"], "output.txt")
    encoder.encode()
    decoder = Decoder("output.txt", "decoded.txt")
    decoder.decode_file()

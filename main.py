import heapq

from decode import Decoder
from node import HuffmanNode, DecodeNode
from collections import deque
import ast
from output_writer import OutputWriter
from encode import Encoder
import os
def dada(path:str):
    fname = []
    for root, directoryNames, fileNames in os.walk(path):
        for file in fileNames:
            fname.append(os.path.join(root, file))
    print(fname)
    return fname
if __name__ == '__main__':
    encoder = Encoder(["input.txt"], "output.txt")
    encoder.encode()
    decoder = Decoder("output.txt", "decoded.txt")
    decoder.decode_file()



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

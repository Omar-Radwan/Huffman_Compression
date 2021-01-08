import filecmp
import heapq
import random

from decode import Decoder
from misc import ENCODING
from node import HuffmanNode, DecodeNode
from collections import deque
import ast
from output_writer import OutputWriter
from encode import Encoder
import os


def dada(path: str):
    fname = []
    for root, directoryNames, fileNames in os.walk(path):
        for file in fileNames:
            fname.append(os.path.join(root, file))
    print(fname)
    return fname


def generate_testcase():
    file1 = "./input.txt"
    file2 = "./input.txt.txt"
    chrs = []
    for i in range(ord('a'), ord('z') + 1):
        chrs.append(chr(i))

    for i in range(ord('A'), ord('Z') + 1):
        chrs.append(chr(i))

    for i in range(ord('0'), ord('9') + 1):
        chrs.append(chr(i))

    while True:
        x = []
        for i in range(10000):
            y = chr(random.randint(0,255))
            x.append(str(y))
        f = open("input.txt", "w",newline='', encoding=ENCODING)
        f.write("".join(x))
        f.close()
        encoder = Encoder(dada("./dir"), "output.txt")
        encoder.encode()
        decoder = Decoder("output.txt")
        decoder.decode_file()
        if not (filecmp.cmp(file1, file2, shallow=False)):
            break


if __name__ == '__main__':
    # choice = int(input('1 - File\n2 - Folder\n'))
    # input_data = ['input.txt'] if choice == 1 else dada('./dir')
    # decoded_data =
    # generate_testcase()
    encoder = Encoder(dada("./dir"), "output.txt")
    encoder.encode()
    decoder = Decoder("output.txt")
    decoder.decode_file()

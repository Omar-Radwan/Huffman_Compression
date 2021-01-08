import filecmp
import heapq
import random
import time

from decode import Decoder
from misc import ENCODING, MB_SIZE, KB_SIZE
from node import HuffmanNode, DecodeNode
from collections import deque
import ast
from output_writer import OutputWriter
from encode import Encoder
import os


def generate_testcase(length: int):
    file1 = "./input.txt"
    file2 = "./input.txt.decoded.txt"
    x = []
    length *= MB_SIZE
    for i in range(length):
        y = chr(random.randint(0, 255))
        x.append(str(y))
    f = open("input.txt", "w", newline='', encoding=ENCODING)
    f.write("".join(x))
    f.close()
    encoder = Encoder(["input.txt"], "output.txt")
    encoder.encode()
    decoder = Decoder("output.txt")
    decoder.decode()
    return (filecmp.cmp(file1, file2, shallow=False))


if __name__ == '__main__':
    # choice = int(input('1 - File\n2 - Folder\n'))
    # input_data = ['input.txt'] if choice == 1 else dada('./dir')
    # decoded_data =

    file1 = "./input.txt"
    file2 = "./input.txt.decoded.txt"
    s1 = time.time()
    encoder = Encoder("./input.txt")
    encoder.encode()
    print(f'encode_time={time.time() - s1}')
    s2 = time.time()
    decoder = Decoder("input.txt.compressed.txt")
    decoder.decode()
    print(f'decode_time={time.time() - s2}')
    print(f'total_time={time.time() - s1}')

    if not (filecmp.cmp(file1, file2, shallow=False)):
        print("Bad")
    else:
        print("Good")
# encoder = Encoder(dada("./dir"), "output.txt")
# encoder.encode()
# decoder = Decoder("output.txt")
# decoder.decode_file()

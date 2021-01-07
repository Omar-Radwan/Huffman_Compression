from collections import deque
from misc import *


class InputReader:
    def __init__(self, file_name, is_decode=True):
        self.buffer = deque([])
        self.file_name = file_name
        self.file = open(self.file_name, "r")
        if is_decode:
            self.line = self.file.read()

    def read_compression_details(self, i):
        if i >= len(self.line):
            return (float('inf'), float('inf'), i)
        # get compressedDataCharacters
        compressedCharactersString = ""
        while self.line[i] != ",":
            compressedCharactersString += str(self.line[i])
            i += 1
        compressedCharacters = int(compressedCharactersString)
        print(compressedCharacters)
        # get number of bits to read from last character
        i += 1
        lastBitsToReadString = ""
        while self.line[i] != ",":
            lastBitsToReadString += self.line[i]
            i += 1
        lastBitsToRead = int(lastBitsToReadString)
        print(lastBitsToRead)
        return compressedCharacters, lastBitsToRead, i+1

    def read_path(self, i):
        if i >= len(self.line):
            return ('', i)
        # number of characters in path
        # file = open(self.file_name, "r")
        huffmanCodes = {}
        # line = file.read()
        pathCharactersString = ""
        while self.line[i] != ",":
            pathCharactersString += str(self.line[i])
            i += 1
        pathCharacters = int(pathCharactersString)
        print(pathCharacters)
        # get path
        i += 1
        path = ""
        while pathCharacters != 0:
            path += str(self.line[i])
            i += 1
            pathCharacters -= 1
        print(path)
        return path, i

    def read_meta_data(self, i) -> ({}, int):
        # 13 k01 c0 d2222 9
        # fileName = "output.txt"
        # file = open(self.file_name, "r")
        huffmanCodes = {}
        # line = file.read()
        # get number of huffmanCodesCharacters
        huffmanCharactersString = ""
        while self.line[i] != DELIM:
            huffmanCharactersString += str(self.line[i])
            i += 1
        huffmanCharacters = int(huffmanCharactersString)
        i += 1
        while huffmanCharacters != 0:
            key = self.line[i]
            value = ""
            i += 1
            huffmanCharacters -= 1
            while self.line[i] != DELIM:
                value += self.line[i]
                i += 1
                huffmanCharacters -= 1
            huffmanCharacters -= 1
            huffmanCodes[value] = key
            i += 1
        print(huffmanCodes)
        return huffmanCodes, i

    def fill_buffer(self, is_clear=True):
        if (is_clear):
            self.buffer.clear()
        read_str = self.file.read(KB_SIZE - len(self.buffer))
        for c in read_str:
            self.buffer.append(c)
        return len(read_str) != 0

    def fill_limited_buffer(self, read_so_far, total_number_of_characters, is_clear=True):
        if (is_clear):
            self.buffer.clear()
        #read_str = self.line[read_so_far:min(KB_SIZE, total_number_of_characters)]
        read_str = self.line[read_so_far:]
        for c in read_str:
            for x in char_to_ascii(c):
                self.buffer.append(x)
        return len(read_str) != 0, read_so_far + len(read_str)

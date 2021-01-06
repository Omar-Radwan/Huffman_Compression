import heapq
from node import HuffmanNode, DecodeNode
from collections import deque
import ast
from output_writer import OutputWriter




if __name__ == '__main__':
    x = ['asd','asd','asda']

    # f = open("input.txt", "r")
    # while True:
    #     ch = f.read(1)
    #     if not ch: break
    #     print(ch)
    # #print(build_huffman_codes(count_char_frequency("input.txt")))
    # # write_compressed_data(build_huffman_codes(count_char_frequency("input.txt")), "input.txt")
    # #frequency = count_char_frequency("input.txt")
    # #huffman_codes = build_huffman_codes(count_char_frequency("input.txt"))
    # #write_meta_data(huffman_codes, frequency, "output.txt")
    # # pq = []
    # # heapq.heappush(pq, 10)
    # # heapq.heappush(pq, 3)
    # # heapq.heappush(pq, 534)
    # # heapq.heappush(pq, 12)
    # # while len(pq) != 0:
    # #     print(heapq.heappop(pq))

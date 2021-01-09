from gui import gui
from encode import Encoder
from decode import Decoder
from compression_ratio import compression_ratio
import time
from interfaceGui import interfaceGui
import os
class controller:
    guiObject=gui()
    guiObject.begin()
    operation=guiObject.operation
    path=guiObject.path.get()
    compression_ratio=compression_ratio()
    s1 = time.time()
    ratio=0
    huffmanCodes={}

    if len(path)!= 0:
        if operation == "compress":
            encoder = Encoder(path)
            encoder.encode()
            ratio = compression_ratio.getCompressionRatio(path, encoder)
            huffmanCodes = encoder.huffman_codes
            print(encoder.huffman_codes)

        else :
            decoder = Decoder(path)
            huffmanCodes = decoder.decode()

        totalTime = time.time() - s1
        print(f'time={time.time() - s1}')
        interfaceGuiObject = interfaceGui(ratio, totalTime, huffmanCodes, operation)

    else :
        print("empty file")





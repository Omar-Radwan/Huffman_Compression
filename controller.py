from gui import gui
from encode import Encoder
from decode import Decoder
from compression_ratio import compression_ratio
import time
from output_gui  import OutputGui
import os
class controller:

    def begin(self):
        guiObject = gui()
        guiObject.begin()
        operation = guiObject.operation
        if type(guiObject.pathh) != str:
            path = guiObject.pathh.get()
            self.solve(path, operation)




    def solve(self,path,operation):
        compression_ratio_object = compression_ratio()
        s1 = time.time()
        ratio = 0


        if len(path) != 0 and os.path.exists(path) and os.stat(path).st_size != 0 :
            if operation == "compress":
                encoder = Encoder(path)
                encoder.encode()
                ratio = compression_ratio_object.getCompressionRatio(path, encoder)
                huffmanCodes = encoder.huffman_codes
                print(encoder.huffman_codes)

            else:
                decoder = Decoder(path)
                huffmanCodes = decoder.decode()

            totalTime = time.time() - s1
            print(f'time={time.time() - s1}')
            output = OutputGui()
            output.displayOutput(ratio, totalTime, huffmanCodes, operation)
            if output.again:
                self.begin()



c=controller()
c.begin()
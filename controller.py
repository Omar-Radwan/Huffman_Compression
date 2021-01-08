from gui import gui
from encode import Encoder
from decode import Decoder

class controller:
    guiObject=gui()
    guiObject.begin()
    operation=guiObject.operation
    path=guiObject.path
    if operation=="compress":
        encoder = Encoder(path)
        encoder.encode()
    else :
        decoder = Decoder(path)
        decoder.decode()

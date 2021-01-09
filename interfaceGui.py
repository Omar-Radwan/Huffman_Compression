from gui import gui
class interfaceGui:
    def __init__(self,ratio,time,huffmanCodes,operation):
        self.ratio=ratio
        self.time=time
        self.huffmanCodes=huffmanCodes
        self.operation=operation
        guiObject=gui()
        guiObject.displayOutput(self.ratio,self.time,self.huffmanCodes,self.operation)
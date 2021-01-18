import tkinter as tk
from tkinter import *

class OutputGui():

    again=False

    def makeLabelPack(self,rootObject, tk, text, row, column, padx, font):
        tk.Label(rootObject,
                 text=text,
                 justify=tk.CENTER,
                 padx=0,
                 font=font,
                 pady=10).pack()

    def displayOutput(self,ratio,time,huffmanCodes,operation):
        root2 = tk.Tk()
        if operation=="compress":
            self.makeLabelPack(root2, tk, "Compression ratio : %s " % (ratio), 26, 1, 0, 15)
        self.makeLabelPack(root2,tk,"Execution time : %s " % (time),27,1,0,15)

        self.makeLabelPack(root2, tk, "Huffman codes ", 28, 1, 0, 15)
        self.makeTable(huffmanCodes, root2,operation)
        tk.Button(root2, text='Back', command=lambda: back()).pack()

        def back():
            root2.destroy()
            self.again=True



        root2.geometry("800x600")
        root2.mainloop()


    def makeTable(self,huffmanCodes:dict, root2,operation):
        h = Scrollbar(root2, orient='horizontal')

        h.pack(side=BOTTOM, fill=X)

        v = Scrollbar(root2)
        v.pack(side=RIGHT, fill=Y)


        t = Text(root2, width=15, height=20, wrap=NONE,
                 xscrollcommand=h.set,
                 yscrollcommand=v.set,
                 font=30)

        for key,value in huffmanCodes.items():
            str=self.formatDictionary(key,value,operation)
            t.insert(END,str)

        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)

    def formatDictionary(self,key,value,operation):
        if operation=="compress":
            return "    '"+key+"'" + "->" + value + "\n \n"
        else :
            return "    "+key+ "->" + "'"+ value +"'"+ "\n \n"

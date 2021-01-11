import tkinter as tk
from tkinter import *


def makeRadioButton(rootObject,tk, text, row, column, value,method):
    tk.Radiobutton(rootObject, text=text, indicatoron=1, width=0, padx=60, variable=method, value=value). \
        grid(row=row, column=column, sticky=tk.W, pady=4)


def makeLabel(rootObject,tk, text, row, column,padx,font):
    tk.Label(rootObject,
             text=text,
             justify=tk.CENTER,
             padx=0,
             font=font,
             pady=10).grid(row=row, column=column, pady=10,padx=padx)

def makeLabelPack(rootObject,tk, text, row, column,padx,font):
    tk.Label(rootObject,
             text=text,
             justify=tk.CENTER,
             padx=0,
             font=font,
             pady=10).pack()
class gui :

    operation = ""
    pathh=""

    def apply(self,method):

        if method.get() == 0:
            self.operation = "compress"
        else:
            self.operation = "Decompress"
        return  self.operation

    def begin(self):
        root = tk.Tk()
        method = tk.IntVar()
        method.set(2)
        path = tk.StringVar()

        makeLabel(root,tk,"Huffman Compression",1,2,50,70)
        makeLabel(root,tk,"Enter name of the file/folder :",10,1,0,20)
        name_entry = tk.Entry(root, textvariable=path, font=('calibre', 10, 'normal'),width=40).grid(row=10, column=2,
                                                                                                   sticky=tk.W, pady=4)
        makeRadioButton(root,tk,"Compress",20,1,0,method)
        makeRadioButton(root,tk,"decompress",21,1,1,method)
        tk.Button(root, text='Apply', command=lambda: checkk()).grid(row=24, column=2, sticky=tk.W, pady=44)

        def checkk():
            self.operation = self.apply(method)
            self.pathh=path
            print(type(self.pathh))
            if len(path.get()) == 0:
                makeLabel(root, tk, "empty path", 25, 2, 0, 15)
            else:
                root.destroy()


        root.geometry("700x600")
        root.mainloop()






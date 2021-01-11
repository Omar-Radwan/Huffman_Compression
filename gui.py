import tkinter as tk
from sys import path
from tkinter import *
from tkinter import messagebox
import os

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
        elif method.get()==1:
            self.operation = "Decompress"
        return  self.operation

    def begin(self):
        root = tk.Tk()
        method = tk.IntVar()
        method.set(2)
        path_input = tk.StringVar()

        makeLabel(root,tk,"Huffman Compression",1,2,50,70)
        makeLabel(root,tk,"Enter name of the file/folder :",10,1,0,20)
        name_entry = tk.Entry(root, textvariable=path_input, font=('calibre', 10, 'normal'),width=40).grid(row=10, column=2,
                                                                                                   sticky=tk.W, pady=4)
        makeRadioButton(root,tk,"Compress",20,1,0,method)
        makeRadioButton(root,tk,"decompress",21,1,1,method)
        tk.Button(root, text='Apply', command=lambda: check()).grid(row=24, column=2, sticky=tk.W, pady=44)

        def check():
            self.operation = self.apply(method)
            self.pathh=path_input
            if len(path_input.get()) == 0:
                messagebox.showinfo("Error", "path is empty")
            elif not os.path.exists(path_input.get()):
                messagebox.showinfo("Error", "path doesn't exist")
            elif os.stat(path_input.get()).st_size == 0:
                messagebox.showinfo("Error", "file is empty")
            elif self.operation=="":
                messagebox.showinfo("Error", "You must choose compress or decompress")


            else:
                root.destroy()


        root.geometry("700x600")
        root.mainloop()




    def alert(self):
        messagebox.showinfo("Error", "file is empty")



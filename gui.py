import tkinter as tk
from sys import path
from tkinter import *
from tkinter import messagebox
import os
from checks import Checks

def makeRadioButton(rootObject, tk, text, row, column, value, method):
    tk.Radiobutton(rootObject, text=text, indicatoron=1, width=0, padx=60, variable=method, value=value). \
        grid(row=row, column=column, sticky=tk.W, pady=4)


def makeLabel(rootObject, tk, text, row, column, padx, font):
    tk.Label(rootObject,
             text=text,
             justify=tk.CENTER,
             padx=0,
             font=font,
             pady=10).grid(row=row, column=column, pady=10, padx=padx)


def makeLabelPack(rootObject, tk, text, row, column, padx, font):
    tk.Label(rootObject,
             text=text,
             justify=tk.CENTER,
             padx=0,
             font=font,
             pady=10).pack()


class gui:
    operation = ""
    pathh = ""

    def apply(self, method):

        if method.get() == 0:
            self.operation = "compress"
        elif method.get() == 1:
            self.operation = "Decompress"
        return self.operation

    def begin(self):
        root = tk.Tk()
        method = tk.IntVar()
        method.set(2)
        path_input = tk.StringVar()
        file_one=tk.StringVar()
        file_two=tk.StringVar()
        checks = Checks()

        makeLabel(root,tk,"Huffman Compression",1,2,50,70)
        makeLabel(root,tk,"Enter name of the file/folder :",10,1,0,20)
        name_entry = tk.Entry(root, textvariable=path_input, font=('calibre', 10, 'normal'),width=40).grid(row=10, column=2,
                                                                                                   sticky=tk.W, pady=4)
        makeRadioButton(root,tk,"Compress",20,1,0,method)
        makeRadioButton(root,tk,"decompress",21,1,1,method)
        tk.Button(root, text='Apply', command=lambda: check()).grid(row=24, column=2, sticky=tk.W, pady=44)
        makeLabel(root, tk, "Huffman Compression", 1, 2, 50, 70)
        makeLabel(root, tk, "Enter name of the file/folder :", 10, 1, 0, 20)
        name_entry = tk.Entry(root, textvariable=path_input, font=('calibre', 10, 'normal'), width=40).grid(row=10,
                                                                                                            column=2,
                                                                                                            sticky=tk.W,
                                                                                                            pady=4)
        makeRadioButton(root, tk, "Compress", 20, 1, 0, method)
        makeRadioButton(root, tk, "Decompress", 21, 1, 1, method)
        tk.Button(root, text='Apply', command=lambda: check()).grid(row=24, column=2, sticky=tk.W, pady=44)
        makeLabel(root, tk, "Compare two files :", 29, 1, 0, 10)
        makeLabel(root, tk, "File one :", 30, 1, 0, 10)
        makeLabel(root, tk, "File two :", 31, 1, 0, 10)
        name_entry = tk.Entry(root, textvariable=file_one, font=('calibre', 10, 'normal'), width=40).grid(row=30,column=2,
                                                                                                            sticky=tk.W,
                                                                                                            pady=4)
        name_entry = tk.Entry(root, textvariable=file_two, font=('calibre', 10, 'normal'), width=40).grid(row=31,column=2,
                                                                                                            sticky=tk.W,
                                                                                                            pady=4)

        tk.Button(root, text='Compare', command=lambda: compare()).grid(row=32, column=2, sticky=tk.W, pady=44)



        def compare():
            if checks.file_one_equal_file_two(file_one.get(),file_two.get()):
                makeLabel(root, tk, "Files are equal.", 32, 3, 0, 10)
            else:
                makeLabel(root, tk, "Files aren't equal.", 32, 3, 0, 10)

        def check():
            self.operation = self.apply(method)
            self.pathh=path_input

            if checks.path_length(path_input)==0:
                messagebox.showinfo("Error", "path is empty")
            elif not checks.path_exists(path_input):
                messagebox.showinfo("Error", "path doesn't exist")
            elif checks.path_empty(path_input):
                messagebox.showinfo("Error", "file is empty")
            elif checks.operation_chosen(self.operation)=="":
                messagebox.showinfo("Error", "You must choose compress or decompress")


            else:
                root.destroy()

        root.geometry("800x600")
        root.mainloop()




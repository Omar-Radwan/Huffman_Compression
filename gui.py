import tkinter as tk

root = tk.Tk()
method = tk.IntVar()
method.set(2)
def makeRadioButton(tk, text, row, column, value):
    tk.Radiobutton(root, text=text, indicatoron=1, width=0, padx=60, variable=method, value=value). \
        grid(row=row, column=column, sticky=tk.W, pady=4)


def makeLabel(tk, text, row, column,padx,font):
    tk.Label(root,
             text=text,
             justify=tk.CENTER,
             padx=10,
             font=font,
             pady=10).grid(row=row, column=column, pady=20,padx=padx)



class gui :

    path = tk.StringVar()
    operation = ""

    def apply(self):

        if method.get() == 0:
            self.operation = "compress"
        else:
            self.operation = "Decompress"
        return self.path.get(), self.operation

    def begin(self):
        makeLabel(tk,"Huffman Compression",1,2,50,70)
        makeLabel(tk,"Enter name of the file/folder :",10,1,0,20)
        name_entry = tk.Entry(root, textvariable=self.path, font=('calibre', 10, 'normal'),width=40).grid(row=10, column=2,
                                                                                                   sticky=tk.W, pady=4)
        makeRadioButton(tk,"Compress",20,1,0)
        makeRadioButton(tk,"decompress",21,1,1)
        tk.Button(root, text='Apply', command=self.start).grid(row=24, column=2, sticky=tk.W, pady=44)

        root.geometry("700x600")
        root.mainloop()


    def start(self):
        self.path,self.operation=self.apply()


import tkinter as tk
from tkinter import *
root = tk.Tk()
method = tk.IntVar()
method.set(2)

def makeRadioButton(rootObject,tk, text, row, column, value):
    tk.Radiobutton(rootObject, text=text, indicatoron=1, width=0, padx=60, variable=method, value=value). \
        grid(row=row, column=column, sticky=tk.W, pady=4)


def makeLabel(rootObject,tk, text, row, column,padx,font):
    tk.Label(rootObject,
             text=text,
             justify=tk.CENTER,
             padx=0,
             font=font,
             pady=10).grid(row=row, column=column, pady=10,padx=padx)

def makeLabel2(rootObject,tk, text, row, column,padx,font):
    tk.Label(rootObject,
             text=text,
             justify=tk.CENTER,
             padx=0,
             font=font,
             pady=10).pack()
class gui :

    path = tk.StringVar()
    operation = ""
    ratio=""

    def apply(self):

        if method.get() == 0:
            self.operation = "compress"
        else:
            self.operation = "Decompress"
        return self.path.get(), self.operation

    def begin(self):
        makeLabel(root,tk,"Huffman Compression",1,2,50,70)
        makeLabel(root,tk,"Enter name of the file/folder :",10,1,0,20)
        name_entry = tk.Entry(root, textvariable=self.path, font=('calibre', 10, 'normal'),width=40).grid(row=10, column=2,
                                                                                                   sticky=tk.W, pady=4)
        makeRadioButton(root,tk,"Compress",20,1,0)
        makeRadioButton(root,tk,"decompress",21,1,1)
        tk.Button(root, text='Apply', command=self.start).grid(row=24, column=2, sticky=tk.W, pady=44)

        root.geometry("700x600")
        root.mainloop()


    def start(self):
        self.path,self.operation=self.apply()
        root.destroy()


    def displayOutput(self,ratio,time,huffmanCodes,operation):
        print(ratio)
        root2 = tk.Tk()
        if operation=="compress":
            makeLabel2(root2, tk, "Compression ratio : %s " % (ratio), 26, 1, 0, 15)
        makeLabel2(root2,tk,"Execution time : %s " % (time),27,1,0,15)

        makeLabel2(root2, tk, "Huffman codes ", 28, 1, 0, 15)
        self.makeTable(huffmanCodes, root2,operation)


        root2.geometry("800x600")
        root2.mainloop()


    def makeTable(self,huffmanCodes:dict, root2,operation):
        h = Scrollbar(root2, orient='horizontal')

        h.pack(side=BOTTOM, fill=X)

        v = Scrollbar(root2)
        v.pack(side=RIGHT, fill=Y)


        t = Text(root2, width=15, height=15, wrap=NONE,
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



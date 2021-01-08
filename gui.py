import tkinter as tk

root = tk.Tk()

class gui :
    def makeRadioButton(tk, text, row, column, value):
        tk.Radiobutton(root, text=text, indicatoron=1, width=0, padx=60, variable=method, value=value). \
            grid(row=row, column=column, sticky=tk.W, pady=4)

    def makeLabel(tk, text, row, column):
        tk.Label(root,
                 text=text,
                 justify=tk.CENTER,
                 padx=10,
                 pady=10).grid(row=row, column=column, sticky=tk.W, pady=4)
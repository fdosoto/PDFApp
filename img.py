# GUI for pdfcreate
import os

import tkinter as tk
from tkinter import filedialog


root = tk.Tk()

label = tk.Label(root, text="File name: ")
label.pack()

v = tk.StringVar()
entry = tk.Entry(root, textvariable=v)
entry.pack()

content = tk.Text(root)
content.pack()
content.insert("0.0", pc.text)

def create_pdf():
    if v.get() == "":
        v.set("example")
    if ".pdf" not in v.get():
        name, doc = pc.make_doc(v.get() + ".pdf")
    else:
        name, doc = pc.make_doc(v.get())
    pc.show(content.get("0.0", tk.END))
    os.startfile(name)


def get_template():
    try:
        filename = filedialog.askopenfilename(
            initialdir=".")
        with open(filename) as file:
            file = file.read()
        content.delete("0.0", tk.END)
        content.insert("0.0", file)
    except:
        pass

b1 = tk.Button(
    root,
    text="Get a template",
    command=get_template)
b1.pack()

button = tk.Button(
    root,
    text="Create PDF",
    command = create_pdf)
button.pack()



root.mainloop()

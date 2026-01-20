import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry("450x350")
root.title("Notes")


label = tk.Label(root, text = "", font = ("ALGERIAN", 14))
label.pack()

def save_note():
    content = text_Area.get("1.0", tk.END)

    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt")])
    
    if file:
        with open(file, 'w') as f:
            f.write(content)


def open_note():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file:
        with open(file, 'r') as f:
            content = f.read()
        
        text_Area.delete("1.0", tk.END)
        text_Area.insert(tk.END, content)

def new_note():
    text_Area.delete("1.0", tk.END)
    text_Area.focus()

toolbar =tk.Frame(root)
toolbar.pack(fill='x')

open_button = tk.Button(toolbar, text="Open Note", command=open_note)
open_button.pack(side='left', padx=5, pady=5)

save_button = tk.Button(toolbar, text="Save Note", command=save_note)
save_button.pack(side='left', padx=5, pady=5)

new_button = tk.Button(toolbar, text="New Note", command=new_note)
new_button.pack(side='left', padx=5, pady=5)

text_Area = tk.Text(root)
text_Area.pack(expand=True, fill='both')

root.mainloop()
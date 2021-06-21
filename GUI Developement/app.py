import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello")


root = tk.Tk()
root.title('First GUI App')


enter_button = ttk.Button(root, text='Enter', command=greet)
enter_button.pack(side='left', fill='x', expand=True)


exit_button = ttk.Button(root, text='Exit', command=root.destroy)
exit_button.pack(side='left', fill='x', expand=True)  # We can also use 'right'

root.mainloop()


"""
pack(): - Next, we call the pack() method on this widget.
This tells it to size itself to fit the given text, and make itself visible.
It just tells the geometry manager to put widgets in the same row or column.
It’s usually the easiest to use if you just want one or a few widgets to appear.
"""
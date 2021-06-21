import tkinter as tk
from tkinter import ttk


root = tk.Tk()   
root.title('MY GUI APP')  # title for our gui window


"""
The application window does not appear before you enter the main loop.
This method says to take all the widgets and objects we created, render them on our screen, and respond to any interactions.
The program stays in the loop until we close the window.
"""
root.mainloop()   

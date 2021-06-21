import tkinter as tk

root = tk.Tk()
root.title("Pack")

# -- Aligning with `side` ---
"""
tk.Label(root, text='Label1', bg='blue').pack(side='left')
tk.Label(root, text='Label1', bg='brown').pack(side='top')
"""


# -- Filling in one direction --
"""
tk.Label(root, text='Label 1', bg='blue').pack(side="left", fill="y")
tk.Label(root, text='Label 2', bg='brown').pack(side='top', fill='x')
"""

# -- Filling in both directions --
"""
tk.Label(root, text="Label 1", bg="yellow").pack(side='left', fill="both")
tk.Label(root, text="Label 2", bg="pink").pack(side='top', fill="both")
"""

# -- Even if either label doesn't fill --

"""
tk.Label(root, text="Label 1", bg="black").pack(side='left')
tk.Label(root, text="Label 2", bg="white").pack(side='top', fill="both")
"""

"""
tk.Label(root, text="Label 1", bg="black").pack(side='left', fill="both")
tk.Label(root, text="Label 2", bg="white").pack(side='top')
"""


# -- expand can make it grow as much as possible.
#  It won't hide other widgets, but other widgets will be compressed --
"""
tk.Label(root, text="Label 1", bg="purple").pack(side='left', fill="both", expand=True)
tk.Label(root, text="Label 2", bg="orange").pack(side='top')
"""


# -- expanding two widgets means they share the available space evenly --

"""
tk.Label(root, text="Label 2", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label 2", bg="green").pack(side="top", expand=True, fill="both")
"""


# -- whichever side comes first gets expansion priority --


"""
tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")
tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
"""

tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")


root.mainloop()



# As you can see, even though we specificied `side="left"`, the last label was still underneath.
# We can't just use packing on the root to take care of all our layout needs.
# Hence, Tkinter has `Frame`, which is a container for other widgets.

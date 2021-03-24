import tkinter as tk
from tkinter import messagebox

# Create the master object
master = tk.Tk()

# Sets the window size as "300x300"
master.geometry("300x300")


# This is the button callback function
# This must be visible to the button, so we must define it before the button widget!
def buttonCallback():
    messagebox.showinfo("Message", "You have clicked the Button!")


# Create a Button widget
button = tk.Button(master, text="Click")

# And a label for it
label_1 = tk.Label(master, text="Simple Button")

# Use the grid geometry manager to put the widgets in the respective position
label_1.grid(row=0, column=0)
button.grid(row=1, column=0)

# The application mainloop
tk.mainloop()
import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click():
	messagebox.showinfo("Info", "I will close your application")
	root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Hello World App")

# Create a label widget with the text
label = tk.Label(root, text="Hello, Ricardo Moreno")
label.pack(pady=20)

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack(side=tk.LEFT, padx=10)

# Create a button widget
button = tk.Button(root, text="OK", command=on_button_click)
button.pack(side=tk.LEFT)

# Run the main event loop
root.mainloop()
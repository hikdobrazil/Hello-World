import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Hello World App")

# Create a label widget with the text
label = tk.Label(root, text="Hello, Ricardo Moreno")
label.pack(pady=20)

# Run the main event loop
root.mainloop()
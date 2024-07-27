import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Hello World GUI")

# Create a label widget with the text "Hello, Ricardo"
label = tk.Label(root, text="Hello, Ricardo")
label.pack(pady=20)

# Run the main event loop
root.mainloop()
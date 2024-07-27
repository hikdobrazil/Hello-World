import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Quiz Game")

# Define the quiz questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "What is the capital of Germany?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Berlin"},
    {"question": "What is the capital of Spain?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Madrid"},
    {"question": "What is the capital of Italy?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Rome"},
    {"question": "What is the capital of Portugal?", "options": ["Lisbon", "Madrid", "Paris", "Rome"], "answer": "Lisbon"},
    {"question": "What is the capital of the United Kingdom?", "options": ["Berlin", "London", "Paris", "Rome"], "answer": "London"},
    {"question": "What is the capital of the United States?", "options": ["Berlin", "Madrid", "Washington, D.C.", "Rome"], "answer": "Washington, D.C."},
    {"question": "What is the capital of Canada?", "options": ["Berlin", "Ottawa", "Paris", "Rome"], "answer": "Ottawa"},
    {"question": "What is the capital of Australia?", "options": ["Berlin", "Madrid", "Canberra", "Rome"], "answer": "Canberra"},
    {"question": "What is the capital of Japan?", "options": ["Tokyo", "Madrid", "Paris", "Rome"], "answer": "Tokyo"}
]

current_question_index = 0
score = 0

# Define the function to be called when the submit button is clicked
def on_submit():
    global current_question_index, score
    selected_option = var.get()
    if selected_option == questions[current_question_index]["answer"]:
        score += 100
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", "Incorrect!")
    current_question_index += 1
    if current_question_index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Result", f"Quiz finished! Your score is {score}")
        root.quit()

# Function to load the current question
def load_question():
    question_label.config(text=questions[current_question_index]["question"])
    for i, option in enumerate(questions[current_question_index]["options"]):
        radio_buttons[i].config(text=option, value=option)

# Create the question label
question_label = tk.Label(root, text="")
question_label.pack()

# Create a variable to store the selected option
var = tk.StringVar()

# Create radio buttons for the options
radio_buttons = []
for _ in range(4):
    rb = tk.Radiobutton(root, text="", variable=var, value="")
    rb.pack(anchor="w")
    radio_buttons.append(rb)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Load the first question
load_question()

# Start the main event loop
root.mainloop()
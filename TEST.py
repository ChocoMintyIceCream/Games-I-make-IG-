import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# Define a function to trigger on button click
def on_click():
    label.config(text="Button Clicked!")

# Add a text label
label = tk.Label(root, text="Welcome to Tkinter", font=("Arial", 14))
label.pack(pady=10)

# Add a clickable button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Start the continuous event listening loop
root.mainloop()

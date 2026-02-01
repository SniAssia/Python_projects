import tkinter as tk # Create a window
window = tk.Tk()
# Create a label widget for the window
greeting = tk.Label(text="Python")
# Add the label to the window frame
greeting.pack()
# Keeps focus on window till closed
window.mainloop()
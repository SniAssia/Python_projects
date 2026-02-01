import tkinter as tk

#create a window
window= tk.Tk()
#create a label widget for the window
label = tk.Label(text="please enter your name : ")
#add the label to the window
label.pack()
#keeps focus on window till closed
window.mainloop()
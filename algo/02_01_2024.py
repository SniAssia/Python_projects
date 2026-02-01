
"""
import tkinter as tk
#create a window
window =tk.Tk()
greeting = tk.Label(text= "python",fg="white",bg="black",width=10,height=2)
button=tk.Button(text="text me",fg="black",bg="white",width=10,height=3)
greeting.pack()
button.pack()
window.mainloop()


import tkinter as tk # Create a window
window = tk.Tk()
# Create Label and Entry
label = tk.Label(text="Name")
nameBox = tk.Entry()
# Create Button to get name in entry box
def getName():
    print(nameBox.get())
btnName = tk.Button(text="Print Name", command=getName)
# Pack all widgets to the window
label.pack()
nameBox.pack()
btnName.pack()
window.mainloop()

"""

import tkinter as tk # Create a Window
window = tk.Tk()
# Creates a 3 × 3 grid layout
# Insert Label widgets into grid
for i in range(3):
    for j in range(3):
        label = tk.Label(text=f"Row {i}\nColumn {j}")
        label.grid(row=i,column=j)
window.mainloop()




    
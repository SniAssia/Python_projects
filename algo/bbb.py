import tkinter as tk
window = tk.Tk()
#create a label widjet for the window
#fg refer to variables
label = tk.Label(text="please enter your name",fg="white",bg="black",height=10,width=20)
namebox=tk.Entry()
def getname():
    print(namebox.get())
btname=tk.Button(text="print name",command = getname)

label.pack()
namebox.pack()
btname.pack()
#keeps focus on window till closed
window.mainloop()



from cgitb import text
from tkinter import *
#root is the main window, it comes before anything else. it is the main frame in which all buttons will be present
root =Tk()
def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()

myButton1 =Button(root,text="Weeknd " ,state=DISABLED, padx=50, pady=5)
myButton2 =Button(root,text="Abel X.O " ,padx=50, pady=50, command=myClick())
myButton1.pack()
myButton2.pack()
root.mainloop()
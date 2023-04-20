from tkinter import *
#root is the main window, it comes before anything else. it is the main frame in which all buttons will be present
root =Tk()
#creating a label widget 
myLabel1 = Label(root, text="hello world")
myLabel2 = Label(root, text="put that cocain on the plate")

#shoving the created label onto the screen
myLabel1.pack()
myLabel2.pack()

root.mainloop()

from tkinter import *

def click():
    print("arsch")
    
window = Tk()

button = Button(window, text="arsch", command=click)
button.pack()

window.mainloop()
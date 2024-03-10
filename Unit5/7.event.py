#Event-Driven Programming
#There is a main loop that looks for events and calls a special function
# whenever an event is detected (principal programming paradigm used in
# Graphical User Interface (GUI) programming
from tkinter import *
import ctypes  # An included library with Python install.
def clickButton():
    ctypes.windll.user32.MessageBoxW(0, "Button Clicked", "Message", 1)
    print("Button Clicked")
w = Tk()
l = Label(w, text = "Event-Driven Programming")
b = Button(w, text = "Click here",command=clickButton)
l.pack()
b.pack()
w.mainloop()
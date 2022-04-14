from tkinter import *
import random

root = Tk()
root.title("Random Colors and Colors")
root.geometry("800x800")

label_name = Label(root, font=(30))
label_name.place(relx = 0.5, rely = 0.3, anchor=CENTER)

class Parent:
    def __init__(self):
        self._score = 0
    def UpdateColors(self):
        self.text = ["BLACK", "RED", "BLUE", "GRAY", "GREEN", "PINK"]
        self.random_text = random.randint(0,5)
        self.colors = ["blue", "black", "red", "gray", "green", "pink"]
        self.random_color = random.randint(0,5)
        label_name["text"] = self.text[self.random_text]
        label_name["fg"] = self.colors[self.random_color]
        
obj = Parent()
btn = Button(root, text = "Change", command=obj.UpdateColors)
btn.place(relx = 0.7, rely = 0.4, anchor=E)

root.mainloop()
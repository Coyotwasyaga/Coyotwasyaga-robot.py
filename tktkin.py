from tkinter import *
import tkinter as tk
from tkinter.filedialog import *
import fileinput
from random import randint
class But_print():

    def __init__(self):
        self.but = Button(root,bg="green")
        self.but["text"] = "Кнопочка!"
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()

    def printer(self,event):
        print("Ну это понятно,что хуйня очередная")


def _open():
    op = askopenfilename()
    for i in fileinput.input(op):
        txt.insert(END, i)



root = Tk()
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open", command=_open)
hm = Menu(m)
m.add_cascade(label="Quit", menu=hm)
hm.add_command(label="Quit", command=quit)
txt = Text(root,width=400,height=150,font="12")
txt.pack()
root.mainloop()


def motion():

    global x, y, R, dx, dy
    x = +dx
    y = +dy
    if  x + R >= 70 or x + R >= 700:
        dx = -dx
    if y + R >=  50 or y + R >= 500:
        dy = -dy
    ball_id = canvas.create_oval(x + R, y + R, x - R, y - R, fill="darkgreen")
    ball_id2 = canvas.create_oval(x - .5*R, y + .5*R, x + .5*R, y - .5*R, fill="darkblue")
    canvas.move(ball_id2, -dx, -dy)
    canvas.move(ball_id, dx, dy)
    root.after(80, motion)


def main():
    WIDTH = 800
    HEIGHT = 600
    global root, canvas
    global x, y, R, dx, dy
    root = tk.Tk()
    che1 = Checkbutton(root, text='Milo', bg="yellow", onvalue=1, offvalue="-")
    rad1 = Radiobutton(root, text="Radio", bg="darkblue", value=1)
    rad2 = Radiobutton(root, text="Video", bg="red", value=0)
    root.geometry("800x600")
    root.config(bg="darkblue")
    canvas = tk.Canvas(root)
    canvas.config(bg="black")
    canvas.pack(anchor='nw', fill=tk.BOTH)
    R = randint(30, 110)
    x = randint(R, 360)
    y = randint(R, 380)
    dx, dy = (+2, +4)
    che1.pack()
    rad1.pack()
    rad2.pack()
    obj = But_print()
    motion()
    root.mainloop()

if __name__ == "__main__":
    main()

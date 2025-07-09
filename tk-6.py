from tkinter import *
window = Tk()

lbl1 = Label(window, text="레이블입니다")
btn1 = Button(window, text="One")
btn2 = Button(window, text="Two")

lbl1.pack()
btn1.pack(side=LEFT, padx=10)
btn2.pack(side=RIGHT, padx=10)

window.mainloop()
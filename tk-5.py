from tkinter import *
window = Tk()

lbl1 = Label(window, text="레이블입니다")
lbl2 = Button(window, text="1번 버튼")
lbl3 = Button(window, text="2번 버튼")

lbl1.pack()
lbl2.pack()
lbl3.pack()

window.mainloop()
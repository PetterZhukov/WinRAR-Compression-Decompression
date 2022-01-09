from tkinter import *
import UI.view_InitFrame

root=Tk()
root.geometry('600x550+500+240')
root.title("初始化程序")

UI.view_InitFrame.InitFrame(root).pack()
root.mainloop()


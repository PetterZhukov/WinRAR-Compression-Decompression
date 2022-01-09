from tkinter import *
import UI.view_InitFrame

def main_Init():
    root=Tk()
    root.geometry('600x550+500+240')
    root.title("初始化程序")

    UI.view_InitFrame.InitFrame(root).pack()
    root.mainloop()

if __name__=='__main__':
    main_Init()


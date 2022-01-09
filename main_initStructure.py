from tkinter import *
import UI.view_InitFrame

def main_Frame()->Tk:
    root=Tk()
    root.geometry('600x500+600+240')
    root.title("初始化程序")
    UI.view_InitFrame.InitFrame(root).pack()
    return root

if __name__=='__main__':
    root=main_Frame()
    root.mainloop()


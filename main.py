from os import system
from tkinter import messagebox
from UI.MainPage import *
from tkinter import *
import fileIO.fileDel as fileDel
import main_initStructure


class process:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("进入enter")
        return Tk()

    def do_self(self):
        print(self.name)

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出exit")
        print("exit information -> ", exc_type, exc_value)
        fileDel.del_file(const.workspacePath)


# root = Tk()
# root.title("解压/压缩小程序")
# MainPage(root)
# root.mainloop()
# # 为了防止内存泄漏,清空workspace
# initModel.del_file(const.workspace)
try:
    with process('process') as root:
        root.title("解压/压缩小程序")
        MainPage(root)
        root.mainloop()
except:
    print("异常 -error")
    root.destroy()
    initRoot=main_initStructure.main_Frame()
    messagebox.showwarning(
        title="警告",message="打开主界面遇到了问题,可以尝试通过初始化页面初始化设置来尝试解决问题\n完成初始化后请重启程序"
        ,parent=initRoot)
    initRoot.mainloop()
    


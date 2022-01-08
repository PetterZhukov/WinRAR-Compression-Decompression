from os import system
from UI.MainPage import *
from tkinter import *
import constValue.constValue as cosnt
import functionModel.initModel as initModel
import fileIO.fileDel as fileDel

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

system("pause")

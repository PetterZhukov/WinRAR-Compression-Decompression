from fileIO.fileIO import LocationJson
from classDesign.password import password
import functionModel.DeCompressModel as decom
from UI.MainPage import *
from tkinter import *
from tkinter import *
import fileIO.fileDel as fileDel


if False:
    initFileStructure()

if False:
    Compress(r"C:\Users\Zhukov\Desktop\Code\VS Code\日常用 py\python解压zip\example_try_rar",
             r"C:\Users\Zhukov\Desktop\Code\VS Code\日常用 py\python解压zip", "save2", 'a123', 'a123')

if False:
    decom.DeCompress(r"C:\Users\Zhukov\Desktop\Code\VS Code\日常用 py\python解压zip\unrar_example\example_try_rar Check_86_94 a123 a123.zip",
    r"C:\Users\Zhukov\Desktop\Code\VS Code\日常用 py\python解压zip\unrar_example",r"save","a123","a123")


if True:
    root = Tk()
    root.title("解压/压缩小程序")
    MainPage(root)
    root.mainloop()

    # 为了防止内存泄漏,清空workspace
    fileDel.del_file(const.workspacePath)

if False:
    PasswordJson.pushPasswordDump_ToFile([password("Default","a123","a123")])
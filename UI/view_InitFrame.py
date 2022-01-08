import os
from tkinter import ttk
import tkinter.filedialog
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox


import constValue.constValue as const
import constValue.readme as readme
import fileIO.fileDel as fileDel
from fileIO.fileIO import LocationJson, PasswordJson, writeStrToFile
import functionModel.initModel as initModel
import fileIO.fileStructure as fileStructure
from classDesign.password import password


class InitFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.defaultPath = StringVar()
        self.passwordName = StringVar()
        self.password1 = StringVar()
        self.password2 = StringVar()
        self.passwordDict = PasswordJson.getPasswordLoad_byFile()

        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="初始化",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="文件结构", font=('宋体', 13, 'bold')
              ).grid(row=row, columnspan=5, sticky=W, pady=5)

        row += 1
        Button(self, text="初始化文件结构",
               command=initModel.initFileStructure_Dir).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="设置文件", font=('宋体', 13, 'bold')
              ).grid(row=row, columnspan=5, sticky=W, pady=5)

        row += 1
        Button(self, text="初始化密码设置",
               command=lambda:
               initModel.initFile_Password() if
               tkinter.messagebox.askokcancel("警告", "存储的密码都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        Button(self, text="初始化路径设置",
               command=lambda:
               initModel.initFile_Location() if
               tkinter.messagebox.askokcancel("警告", "存储的路径都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        Button(self, text="初始化其他设置",
               command=lambda:
               initModel.initFile_Flag() if
               tkinter.messagebox.askokcancel("警告", "存储的其他设置都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        Button(self, text="初始化所有设置",
               command=lambda:
               initModel.initFileStructure_AllFile() if
               tkinter.messagebox.askokcancel("警告", "存储的所有的设置都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="资源文件夹", font=('宋体', 13, 'bold')
              ).grid(row=row, columnspan=5, sticky=W, pady=5)

        row += 1
        Button(self, text="初始化工作区",
               command=lambda:
               initModel.clear_workspace() if
               tkinter.messagebox.askokcancel("警告", "工作区的文件将会被清空，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        Button(self, text="初始化输出区",
               command=lambda:
               initModel.clear_output() if
               tkinter.messagebox.askokcancel("警告", "输出区的文件将被清空，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)
        Button(self, text="预览位置", command=lambda:tkinter.filedialog.askdirectory(initialdir=const.outputPath)
               ).grid(
            row=row, column=1, padx=10)
        # row += 1
        # Button(self, text="init readme.txt", command=self.init_readme).grid(
        #     row=row, stick=W, pady=2)

        # row += 1
        # Label(self, text="默认压缩到:").grid(row=row, sticky=W)

        # row += 1
        # Entry(self, textvariable=self.defaultPath).grid(row=row)
        # Button(self, text="预览",
        #        command=self.get_Location).grid(row=row, column=1, stick=W, pady=2, padx=5)

        # Button(self, text="修改默认压缩路径",
        #        command=self.change_defaultLocation).grid(row=row, column=2, stick=W, pady=2)

        # row += 1
        # Button(self, text="初始化所有数据文件", command=self.init_readme).grid(
        #     row=row, stick=W, pady=2)

        # row += 1
        # Button(self, text="建立文件夹结构", command=self.init_readme).grid(
        #     row=row, stick=W, pady=2)

        # row += 1
        # Button(self, text="清空程序工作区(避免内存泄漏)", command=self.initWorkspace).grid(
        #     row=row, stick=W, pady=2)

    # def get_Location(self):
    #     "可视化选择文件夹"
    #     self.defaultPath.set(tkinter.filedialog.askdirectory())

    # def read_defaultLocation(self):
    #     "从DefaultLocationPath中读默认路径"
    #     self.defaultPath.set(LocationJson.getLocationDefault())

    # def change_defaultLocation(self):
    #     "get dirname"
    #     with open(const.DefaultLocationPath, 'w') as f:
    #         f.write(os.path.normpath(self.defaultPath.get())+'\\')

    def init_readme_open(self):
        "init readme 并在os中打开"
        initModel.initFile_readme()
        fileStructure.openFileInOS(const.readmePath)

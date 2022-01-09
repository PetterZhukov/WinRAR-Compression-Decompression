import os

from tkinter import *
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox

import fileIO.fileIO as fileIO
import constValue.constValue as const
import constValue.readme as readme
import functionModel.initModel as initModel
import functionModel.initStructureModel as initStructureModel
import fileIO.fileStructure as fileStructure


class OriginFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="开始",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)
        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="提示:", font=('宋体', 13, 'bold')).grid(
            row=row, columnspan=5, sticky=W)
        row += 1
        Text1 = Text(self, width=50, height=8)
        Text1.grid(row=row, column=0, columnspan=5, rowspan=4)
        Text1.insert("end", readme.originTips)
        Text1['state'] = 'disabled'

        row += 4
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=5, sticky='EW', pady=20)

        row += 1
        Label(self, text="本程序基于winrar软件,点击以下按钮确认winrar的安装", font=(
            '宋体', 10, 'bold')).grid(row=row, columnspan=5, sticky=W)

        row += 1
        Button(self, text="define WinRar and Rar",
               command=self.define_WinRar).grid(row=row, stick=EW, pady=2)

        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=5, sticky='EW', pady=20)

        row += 1
        Label(self, text="点击以进行最开始的初始化", font=('宋体', 10, 'bold')).grid(
            row=row, sticky=W, columnspan=2)

        row += 1
        Button(self, text="初始化以继续",
               command=lambda:
               (lambda: (initStructureModel.initFileStructure_Dir(),
                         fileIO.FlagJson.setFirstOpen(False)))()
               if tkinter.messagebox.askokcancel("初始化", "初始化文件结构和配置文件")
               else None
               ).grid(
            row=row, column=0, stick=W, pady=2, sticky=EW)

        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=5, sticky='EW', pady=20)

        row += 1
        Label(self, text="点击查看说明文档", font=('宋体', 10, 'bold')).grid(
            row=row, sticky=W, columnspan=2)

        row += 1
        Button(self, text="查看说明文档readme", command=self.init_readme_open).grid(
            row=row, column=0, stick=EW, pady=2)

    def define_WinRar(self):
        "define the install and path of Winrar and rar"
        tkinter.messagebox.showinfo(title="结果",
                                    message=("X path未配置WinRar" if os.system("winrar") == 1
                                             else "√ path已经配置WinRar")+'\n' +
                                    ("X path未配置Rar" if os.system("rar") == 1 else "√ path已经配置Rar"))

    def init_readme_open(self):
        "init readme 并在os中打开"
        initModel.initFile_readme()
        fileStructure.openFile(const.readmePath)

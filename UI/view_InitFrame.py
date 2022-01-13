import os
import tkinter.ttk
import tkinter.filedialog
from tkinter import *
import tkinter.messagebox


import constValue.constValue as const
import functionModel.initModel as initModel
import functionModel.initStructureModel as initStructureModel
import fileIO.fileStructure as fileStructure
import fileIO.fileIO as fileIO


class InitFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="初始化",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)

        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="点击查看说明文档", font=('宋体', 10, 'bold')).grid(
            row=row, sticky=W, columnspan=2)

        row += 1
        Button(self, text="查看说明文档readme", command=self.init_readme_open).grid(
            row=row, column=0, stick=EW, pady=2)
        
        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="文件结构", font=('宋体', 13, 'bold')
              ).grid(row=row, columnspan=5, sticky=W, pady=5)

        row += 1
        Button(self, text="初始化文件结构",
               command=initStructureModel.initFileStructure_Dir).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="设置文件", font=('宋体', 13, 'bold')
              ).grid(row=row, columnspan=5, sticky=W, pady=5)

        row += 1
        Button(self, text="初始化密码设置",
               command=lambda:
               (lambda: (
                   initModel.initFile_Password(),
                   tkinter.messagebox.showinfo("提示", "初始化密码设置成功"))
                )() if
               tkinter.messagebox.askokcancel("警告", "存储的密码都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        Button(self, text="初始化路径设置",
               command=lambda:
               (lambda: (
                   initModel.initFile_Location(),
                   tkinter.messagebox.showinfo("提示", "初始化路径设置成功"))
                )()
                   if
               tkinter.messagebox.askokcancel("警告", "存储的路径都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=1, stick=W, pady=2, padx=10)

        row += 1
        Button(self, text="初始化其他设置",
               command=lambda:
               (lambda: (
                   initModel.initFile_Flag(), tkinter.messagebox.showinfo("提示", "初始化其他设置成功"))
                )()
                   if
               tkinter.messagebox.askokcancel("警告", "存储的其他设置都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        Button(self, text="初始化所有设置",
               command=lambda:
               (lambda: (
                   initStructureModel.initFileStructure_AllFile(),
                   tkinter.messagebox.showinfo("提示", "初始化所有设置成功"))
                )()
                   if
               tkinter.messagebox.askokcancel("警告", "存储的所有的设置都会被初始化，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2, columnspan=2, sticky=EW)

        row += 1
        tkinter.ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="资源文件夹", font=('宋体', 13, 'bold')
              ).grid(row=row, columnspan=5, sticky=W, pady=5)

        row += 1
        Button(self, text="初始化工作区",
               command=lambda:
               (lambda: (
                   initModel.clear_workspace(), tkinter.messagebox.showinfo("提示", "初始化工作区成功"))
                )()
                   if
               tkinter.messagebox.askokcancel("警告", "工作区的文件将会被清空，是否继续?") else None
               ).grid(
            row=row, column=0, stick=W, pady=2)

        row += 1
        Button(self, text="初始化输出区",
               command=lambda:
               (lambda: (initModel.clear_output(), tkinter.messagebox.showinfo("提示", "初始化输出区成功"))
                )()
               if
               tkinter.messagebox.askokcancel("警告", "输出区的文件将被清空，是否继续?")
               else None
               ).grid(
            row=row, column=0, stick=W, pady=2)
        Button(self, text="查看输出区内容", command=lambda: tkinter.filedialog.askopenfilename(initialdir=const.outputPath)
               ).grid(
            row=row, column=1, sticky=W)

    def init_readme_open(self):
        "init readme 并在os中打开"
        initModel.initFile_readme()
        fileStructure.openFile(const.readmePath)

import os
from tkinter import font, ttk
import tkinter.filedialog
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox


import constValue.constValue as const
import constValue.readme as readme
import fileIO.fileDel as fileDel
from fileIO.fileIO import LocationJson, LocationJson, writeStrToFile
import functionModel.initModel as initModel
import fileIO.fileStructure as fileStructure
from classDesign.password import password


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
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="提示:",font=('宋体', 13, 'bold')).grid(row=row, columnspan=5, sticky=W)
        row += 1
        Text1 = Text(self, width=50, height=8)
        Text1.grid(row=row, column=0, columnspan=5, rowspan=4)
        Text1.insert("end", readme.originTips)
        Text1['state'] = 'disabled'

        row += 4
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=5, sticky='EW', pady=20)

        row += 1
        Label(self, text="本程序基于winrar软件,点击以下按钮确认winrar的安装", font=(
            '宋体', 10, 'bold')).grid(row=row, columnspan=5, sticky=W)

        row += 1
        Button(self, text="define WinRar and Rar",
               command=self.define_WinRar).grid(row=row, stick=W, pady=2)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=5, sticky='EW', pady=20)

        row += 1
        Label(self, text="点击以进行最开始的初始化", font=('宋体', 10, 'bold')).grid(
            row=row, sticky=W, columnspan=2)

        row+=1
        Button(self, text="初始化以继续",
               command=lambda:
               initModel.initFileStructure_AllFile() if
               tkinter.messagebox.askokcancel("初始化", "初始化文件结构和配置文件") else None
               ).grid(
            row=row, column=0, stick=W, pady=2,sticky=EW)
        
        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=5, sticky='EW', pady=20)
        
        row += 1
        Label(self, text="点击查看说明文档", font=('宋体', 10, 'bold')).grid(
            row=row, sticky=W, columnspan=2)
            
        row += 1
        Button(self, text="查看说明文档readme", command=self.init_readme_open).grid(
            row=row, column=0, stick=W, pady=2)

        # ttk.Separator(self,orient='horizontal').grid(row=row,column=0,rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)
        # row += 1
        # Label(self, text="初始化/更改选项", font=('宋体', 13, 'bold')
        #       ).grid(row=row, columnspan=5, sticky=W, pady=10)

        # indent=0

        # row += 1
        # Label(self, text="1.初始化选项", font=('宋体', 10, 'bold')).grid(
        #     row=row, sticky=W, columnspan=2, padx=indent)
        # row += 1
        # Button(self, text="初始化文件夹结构", command=initModel.initFileStructure_Dir).grid(
        #     row=row, column=0, stick=W, pady=2, padx=indent)
        # Button(self, text="初始化所有设置", command=initModel.initFileStructure).grid(
        #     row=row, column=1, stick=W, pady=2)

        # row += 1
        # Label(self, text="2.说明文档", font=('宋体', 10, 'bold')).grid(
        #     row=row, sticky=W, columnspan=2, padx=indent)
        # row += 1
        # Button(self, text="查看说明readme", command=self.init_readme_open).grid(
        #     row=row, column=0, stick=W, pady=2, padx=indent)

        # row += 1
        # Label(self, text="3.管理密码", font=('宋体', 10, 'bold')).grid(
        #     row=row, sticky=W, columnspan=2, padx=indent)

        # row += 1
        # Label(self, text="删除").grid(row=row, sticky=W, columnspan=2, padx=5)
        # self.passwordCBox = Combobox(self, width=25, state='readonly')
        # self.update_passwordCBox()
        # self.passwordCBox.current(0)
        # self.passwordCBox.grid(row=row, column=1, pady=10)
        # Button(self, text="提交删除", command=self.del_password).grid(
        #     row=row, column=2, stick=W, pady=2)

        # row += 1
        # Label(self, text="增加").grid(row=row, sticky=W)

        # row += 1
        # Label(self, text="密码名字(不能重复)").grid(row=row, sticky=W)
        # Entry(self, textvariable=self.passwordName).grid(row=row, column=1)

        # row += 1
        # Label(self, text="密码1(内层) : ").grid(row=row, sticky=W)
        # Entry(self, textvariable=self.password1).grid(row=row, column=1)

        # row += 1
        # Label(self, text="密码2(内层) : ").grid(row=row, sticky=W)
        # Entry(self, textvariable=self.password2).grid(row=row, column=1)

        # row += 1
        # Button(self, text="提交增加", command=self.add_password).grid(
        #     row=row, column=1, stick=W, pady=2)

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

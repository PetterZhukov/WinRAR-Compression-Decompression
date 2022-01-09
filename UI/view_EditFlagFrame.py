import os
from tkinter import ttk
import tkinter.filedialog
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox


import constValue.constValue as const
import constValue.readme as readme
import fileIO.fileDel as fileDel
import functionModel.initModel as initModel
import fileIO.fileStructure as fileStructure
from classDesign.password import password
import fileIO.fileIO as fileIO


class EditFlagFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.FirstPageTuple = (("开始页", const.firstPageName_Origin),
                          ("初始化页", const.firstPageName_Init),
                          ("压缩", const.firstPageName_Compress),
                          ("解压", const.firstPageName_DeCompress)
                          )

        
        self.nowFirstPage=StringVar()
        self.creatPage()
        self.updatenowFirstPage()
    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="修改其他设置",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="设置打开时显示的页面", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=W, columnspan=2, padx=5)
        
        
        row+=1
        Label(self,text="当前开始页 : ").grid(row=row,sticky=E)
        Entry(self,state='disabled',textvariable=self.nowFirstPage).grid(row=row,column=1)

        row+=1
        self.FirstPageChoose = Combobox(self, width=25, state='readonly')
        self.update_passwordCBox()
        self.FirstPageChoose.grid(row=row, column=1, pady=10)
        Button(self, text="选择当前页", command=self.setFirstPage).grid(
            row=row, column=2, stick=W, pady=5, padx=5)

    def updatenowFirstPage(self):
        ch='Serach Fail'
        get=fileIO.FlagJson.getFirstPage()
        for i in self.FirstPageTuple:
            if i[1]==get:
                ch=i[0]
                break
        self.nowFirstPage.set(ch)
    def update_passwordCBox(self):
        self.FirstPageChoose['values'] = self.FirstPageTuple
        self.FirstPageChoose.current(0)
        
    def setFirstPage(self):
        fileIO.FlagJson.setFirstPage(self.FirstPageTuple[self.FirstPageChoose.current()][1])
        self.updatenowFirstPage()
        tkinter.messagebox.showinfo("提示","设置完成")


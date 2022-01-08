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
import fileIO.fileIO as fileIO

class EditLocationFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        
        self.LocationName = StringVar()
        self.LocationIn = StringVar()
        self.LocationDict = fileIO.LocationJson.getLocationLoad_byFile()

        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="修改路径",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="删除", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=W, columnspan=2, padx=5)
        self.LocationCBox = Combobox(self, width=30, state='readonly')
        self.update_LocationCBox()
        self.LocationCBox.current(0)
        self.LocationCBox.grid(row=row, column=1, pady=10)
        Button(self, text="预览位置", command=self.previewToCBoxLoaction).grid(
            row=row, column=2,padx=10)

        row+=1
        Button(self, text="提交删除", command=self.del_Location).grid(
            row=row, column=1,stick=W, pady=5,padx=5)
        row += 1
        Label(self, text="增加", font=('宋体', 13, 'bold')).grid(row=row, sticky=W)

        row += 1
        Label(self, text="路径名字(不能重复) : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.LocationName).grid(row=row, column=1,sticky=W)

        row += 1
        Label(self, text="路径 : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.LocationIn).grid(row=row, column=1,sticky=EW)
        Button(self, text="预览位置", command=self.previewToLocation).grid(
            row=row, column=2,padx=10)
        row += 1
        Button(self, text="提交增加", command=self.add_Location).grid(
            row=row, column=1, stick=W, pady=5)



    def previewToCBoxLoaction(self):
        tkinter.filedialog.askdirectory(initialdir=self.LocationDict[list(self.LocationDict.keys())[self.LocationCBox.current()]])
    def previewToLocation(self):
        self.LocationIn.set(os.path.normpath(tkinter.filedialog.askdirectory())+'\\') 
    def del_Location(self):
        "删除某行Location"
        if tkinter.messagebox.askokcancel("提示", "确认要提交删除？"):
            index = self.LocationCBox.current()
            keyName=list(self.LocationDict.keys())[index]
            self.LocationDict.pop(keyName)
            self.update_LocationCBox()
            self.update_LocationJson()
            tkinter.messagebox.showinfo("提示", "删除成功")

    def add_Location(self):
        "增加Location"
        def getDefaultName():
            for i in range(1, int(1e5)):
                if ("路径"+str(i)) not in self.LocationDict.keys():
                    return "路径"+str(i)
            return "路径"

        if tkinter.messagebox.askokcancel("提示", "确认要提交增加？"):
            if self.LocationName.get() == "":
                self.LocationName.set(getDefaultName())
            if self.LocationName.get() in self.LocationDict.keys():
                tkinter.messagebox.showerror("警告", "路径设定名字不能重名")
            else:
                self.LocationDict[self.LocationName.get()] = self.LocationIn.get()
                self.update_LocationCBox()
                self.update_LocationJson()
                tkinter.messagebox.showinfo("成功", "成功增加路径设定")

    def update_LocationCBox(self):
        "更改Location下拉框的值"
        self.LocationCBox['values'] = [a+':  \"'+b+'\"' for a,b in self.LocationDict.items()]
        self.LocationCBox.current(0)
                                            
    def update_LocationJson(self):
        "将更改提交到Location.json"
        fileIO.LocationJson.pushLoactionDump_ToFile(self.LocationDict) 
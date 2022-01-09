import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox

import constValue.constValue as const

import fileIO.fileIO as fileIO


class EditLocationFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.LocationName = StringVar()
        self.LocationIn = StringVar()
        self.ModelName = StringVar()

        self.creatPage()
        self.setModel_CompressFrom()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        "修改地址 : xxxxxx"
        Label(self, textvariable=self.ModelName,
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0, columnspan=4)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        selectF = Frame(self)
        selectF.grid(row=row, column=0, columnspan=4, pady=10)
        Button(selectF, text="修改'从...压缩'路径", command=self.setModel_CompressFrom).grid(
            row=0, column=0, padx=10)
        Button(selectF, text="修改'压缩到/从...解压'路径", command=self.setModel_CompressTo).grid(
            row=0, column=1, padx=10)
        Button(selectF, text="修改'解压到'路径", command=self.setModel_DeCompressTo).grid(
            row=0, column=2, padx=10)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="删除", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        self.LocationCBox = Combobox(self, width=30)
        self.LocationCBox.grid(row=row, column=1, pady=10)
        Button(self, text="预览位置", command=self.previewToCBoxLoaction).grid(
            row=row, column=2, padx=10)

        row += 1
        Button(self, text="提交删除", command=self.del_Location).grid(
            row=row, column=1, stick=W, pady=5, padx=5)
        row += 1
        Label(self, text="增加", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        row += 1
        Label(self, text="路径名字(不能重复) : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.LocationName).grid(
            row=row, column=1, sticky=W)

        row += 1
        Label(self, text="路径 : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.LocationIn).grid(
            row=row, column=1, sticky=EW)
        Button(self, text="预览位置", command=self.previewToLocation).grid(
            row=row, column=2, padx=10)
        row += 1
        Button(self, text="提交增加", command=self.add_Location).grid(
            row=row, column=1, stick=W, pady=5)

    def previewToCBoxLoaction(self):
        "查看下拉框所在位置"
        tkinter.filedialog.askdirectory(initialdir=self.LocationDict[list(
            self.LocationDict.keys())[self.LocationCBox.current()]])

    def previewToLocation(self):
        "预览输入框网址"
        if self.LocationIn.get() != "":
            self.LocationIn.set(os.path.normpath(
                tkinter.filedialog.askdirectory(initialdir=self.LocationIn.get))+'\\')
        else:
            self.LocationIn.set(os.path.normpath(
                tkinter.filedialog.askdirectory())+'\\')

    def del_Location(self):
        "删除某行Location"
        if tkinter.messagebox.askokcancel("提示", "确认要提交删除？"):
            index = self.LocationCBox.current()
            keyName = list(self.LocationDict.keys())[index]
            if keyName == const.Location_defaultName:
                tkinter.messagebox.showwarning("警告", "不能更改默认值")
            else:
                self.LocationDict.pop(keyName)
                self.update_LocationJson()
                self.update_LocationCBox()
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
                tkinter.messagebox.showwarning("警告", "路径设定名字不能重名")
            else:
                self.LocationDict[self.LocationName.get()
                                  ] = self.LocationIn.get()
                self.update_LocationJson()
                self.update_LocationCBox()
                tkinter.messagebox.showinfo("成功", "成功增加路径设定")

    def update_LocationCBox(self):
        "从LocationJso读信息且更改Location下拉框的值"
        self.LocationDict = self.getLocationdictFun()
        self.LocationCBox['values'] = [a+':  \"'+b +
                                       '\"' for a, b in self.LocationDict.items()]
        self.LocationCBox.current(0)

    def update_LocationJson(self):
        "将更改提交到Location.json"
        self.setLocationjsonFun(self.LocationDict)

    def setModel_CompressFrom(self):
        "将模式更改为 CompressFrom"
        self.ModelName.set("修改路径 : 从...压缩")
        self.getLocationdictFun = fileIO.LocationJson.getCompressFrom
        self.setLocationjsonFun = fileIO.LocationJson.setCompressFrom
        self.update_LocationCBox()

    def setModel_CompressTo(self):
        "将模式更改为 CompressTo"
        self.ModelName.set("修改路径 : 压缩到.../从...解压")
        self.getLocationdictFun = fileIO.LocationJson.getCompressTo
        self.setLocationjsonFun = fileIO.LocationJson.setCompressTo
        self.update_LocationCBox()

    def setModel_DeCompressTo(self):
        "将模式更改为 DeCompressTo"
        self.ModelName.set("修改路径 : 解压到...")
        self.getLocationdictFun = fileIO.LocationJson.getDeCompressTo
        self.setLocationjsonFun = fileIO.LocationJson.setDeCompressFrom
        self.update_LocationCBox()

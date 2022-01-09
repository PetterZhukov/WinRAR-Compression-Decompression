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


class EditPasswordFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.passwordName = StringVar()
        self.password1 = StringVar()
        self.password2 = StringVar()
        self.passwordDict = fileIO.PasswordJson.getPasswordLoad_byFile()

        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="修改密码",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="删除", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=W, columnspan=2, padx=5)
        self.passwordCBox = Combobox(self, width=25, state='readonly')
        self.update_passwordCBox()
        
        self.passwordCBox.grid(row=row, column=1, pady=10)
        Button(self, text="提交删除", command=self.del_password).grid(
            row=row, column=2, stick=W, pady=5,padx=5)

        row += 1
        Label(self, text="增加", font=('宋体', 13, 'bold')).grid(row=row, sticky=W)

        row += 1
        Label(self, text="密码名字(不能重复) : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.passwordName).grid(row=row, column=1)

        row += 1
        Label(self, text="密码1(内层) : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.password1).grid(row=row, column=1)

        row += 1
        Label(self, text="密码2(内层) : ").grid(row=row, sticky=E)
        Entry(self, textvariable=self.password2).grid(row=row, column=1)

        row += 1
        Button(self, text="提交增加", command=self.add_password).grid(
            row=row, column=1, stick=W, pady=5)
        
    def del_password(self):
        "删除某行password"
        if tkinter.messagebox.askokcancel("提示", "确认要提交删除？"):
            index = self.passwordCBox.current()
            keyName=list(self.passwordDict.keys())[index]
            if keyName==const.password_defulatName:
                tkinter.messagebox.showerror("警告","不能更改默认值")
            else:
                self.passwordDict.pop(keyName)
                self.update_PasswordJson()
                self.update_passwordCBox()
                tkinter.messagebox.showinfo("提示", "删除成功")

    def add_password(self):
        "增加password"
        def getDefaultName():
            for i in range(1, int(1e5)):
                if ("密码"+str(i)) not in self.passwordDict.keys():
                    return "密码"+str(i)
            return "密码"

        if tkinter.messagebox.askokcancel("提示", "确认要提交增加？"):
            if self.passwordName.get() == "":
                self.passwordName.set(getDefaultName())
            if self.passwordName.get() in self.passwordDict.keys():
                tkinter.messagebox.showerror("警告", "密码设定名字不能重名")
            else:
                pClass = password(self.passwordName.get(),
                                  self.password1.get(), self.password2.get())
                self.passwordDict[pClass.name] = pClass
                self.update_PasswordJson()
                self.update_passwordCBox()
                tkinter.messagebox.showinfo("成功", "成功增加密码设定")

    def update_passwordCBox(self):
        self.passwordDict = fileIO.PasswordJson.getPasswordLoad_byFile()
        self.passwordCBox['values'] = tuple(map(lambda o: f"{o[0]} : {o[1].password1} {o[1].password2}",
                                                self.passwordDict.items())) 
        self.passwordCBox.current(0)

    def update_PasswordJson(self):
        "将更改提交到password.json"
        fileIO.PasswordJson.pushPasswordDump_ToFile(list(self.passwordDict.values()))                         

import os.path
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo

import constValue.constValue as const
import functionModel.CompressModel as CM
import functionModel.DeCompressModel as DeCM
from fileIO.fileIO import PasswordJson
from fileIO.fileStructure import getStrOfFilePath, openFileInOS
from functionModel import checkModel


class DeCompressFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.From = StringVar()
        self.ToDirname = StringVar()
        self.ToFilename = StringVar()
        self.password1 = StringVar()
        self.password2 = StringVar()

        self.passwordDict = PasswordJson.getPasswordLoad_byFile()
        self.creatPage()

    def creatPage(self):
        """
        //注意事项
        压缩包位置
        解压位置    路径+名字
            默认
            点选文件夹
            输入
        提交/Entry
        """
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="解压",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="选定压缩包").grid(row=row)

        row += 1
        Entry(self, textvariable=self.From).grid(
            row=row, ipadx=80, padx=10, pady=10, columnspan=2)

        Button(self, text="预览位置", command=self.previewFromLocation).grid(
            row=row, column=2)

        row += 1
        Label(self, text="解压路径").grid(row=row, sticky=W, padx=10)

        row += 1
        Entry(self, textvariable=self.ToDirname).grid(
            row=row, ipadx=80, padx=10, pady=10, columnspan=2)
        Button(self, text="预览位置", command=self.previewToLocation).grid(
            row=row, column=2)
        Button(self, text="默认位置", command=self.ReadDefaultLocation).grid(
            row=row, column=3)

        row += 1
        Label(self, text="解压文件名").grid(row=row, sticky=W, padx=10)

        row += 1
        Entry(self, textvariable=self.ToFilename).grid(
            row=row, ipadx=80, padx=10, pady=10, columnspan=2)
        Button(self, text="文件名不变", command=self.getFromDirname).grid(
            row=row, column=2)

        row += 1
        Button(self, text="特殊格式取文件名", command=self.special_getFromDirname).grid(
            row=row, column=1)
        Button(self, text="特殊格式取密码", command=self.special_getPasswordFromName).grid(
            row=row, column=2)

        row += 1
        Label(self, text="第一层(内层)密码 : ").grid(row=row, sticky=E, padx=10)
        Entry(self, textvariable=self.password1).grid(
            row=row, column=1)
        Button(self, text="默认第一层密码", command=self.ReadDefaultPassword1).grid(
            row=row, column=2)
        row += 1
        Label(self, text="第二层(外层)密码 : ").grid(row=row, sticky=E, padx=10)
        Entry(self, textvariable=self.password2).grid(
            row=row, column=1)
        Button(self, text="默认第二层密码", command=self.ReadDefaultPassword2).grid(
            row=row, column=2)

        row += 1
        Label(self, text="密码选择 : ").grid(row=row, sticky=E, padx=10)
        # ttk combox
        self.cbox = ttk.Combobox(self, width=25, state='readonly')
        self.setPasswordBoxValue()
        self.cbox.current(0)
        self.cbox.bind('<<ComboboxSelected>>', self.retPassword)
        self.cbox.grid(row=row, column=1, pady=10)

        row += 1
        Button(self, text="Submit", command=self.submit, width=30).grid(
            row=row, pady=15, columnspan=3, padx=80, sticky=W)

    def getFromDirname(self):
        "从被压缩文件处获得文件名"
        num = os.path.split(self.From.get())
        if len(num) < 2:
            showinfo(title="警告", message="被压缩路径格式错误")
        else:
            self.ToFilename.set(os.path.splitext(num[1])[0])

    def special_getFromDirname(self):
        "根据固定格式更改to文件名"
        name = os.path.split(os.path.splitext(self.From.get())[0])[-1]
        self.ToFilename.set(' '.join(name.split()[:-3]))

    def checkFrom(self):
        "check self.From"
        ch = self.From.get()
        if(ch == ''):
            return '被压缩路径不能为空'
        elif(os.path.exists(ch) == False):
            return '被压缩路径指向的文件/文件夹不存在'
        else:
            return None

    def checkTo(self):
        "check self.To"
        ch = os.path.join(self.ToDirname.get(), self.ToFilename.get())
        if os.path.exists(ch):
            for i in range(1, 1e6):
                if not os.path.exists(os.path.join(self.ToDirname.get(), self.ToFilename.get()+'_'+str(i))):
                    ch = os.path.join(self.ToDirname.get(),
                                      self.ToFilename.get()+str(i))
                    break
            if os.path.exists(ch):
                return '要创建的文件夹和其他文件重名,已更名为不重名的文件名'
            else:
                return '要创建的文件夹和其他文件重名'
        else:
            return None

    def checkPasswordNULL(self):
        "密码非空"
        if self.password1.get() == '':
            return '第一层密码不能为空'
        elif self.password2.get() == '':
            return '第二层密码不能为空'
        return None

    def checkPasswordSpace_change(self):
        "检查密码是否有空格"
        ret = True

        def checkStrspace(ch: str):
            have = False
            if ' ' in ch:
                have = True
                ch = ch.replace(' ', '_')
            return have, ch
        have, ch = checkStrspace(self.password1.get())
        if have:
            self.password1.set(ch)
            ret = False
        have, ch = checkStrspace(self.password2.get())
        if have:
            self.password2.set(ch)
            ret = False
        return ret

    def tk_getFilename(self) -> str:
        "可视化获取文件名  -> 限定了压缩文件的后缀"
        return os.path.normpath(
            tkinter.filedialog.askopenfilename(filetypes=const.filetypes_speial))

    def tk_getDirname(self) -> str:
        "可视化获取文件夹名"
        if self.checkFrom() == None:
            key = os.path.split(self.From.get())[0]
        else:
            key = './/'
        return os.path.normpath(tkinter.filedialog.askdirectory(initialdir=key))+'\\'

    def previewFromLocation(self):
        "预览from"
        self.From.set(self.tk_getFilename())

    def previewToLocation(self):
        "预览to"
        self.ToDirname.set(self.tk_getDirname())

    def ReadDefaultPassword1(self):
        "读默认密码1"
        self.password1.set(
            self.passwordDict[const.password_defulatName].password1
            if const.password_defulatName in self.passwordDict else "No found")

    def ReadDefaultPassword2(self):
        "读默认密码2"
        self.password2.set(
            self.passwordDict[const.password_defulatName].password2
            if const.password_defulatName in self.passwordDict else "No found")

    def ReadDefaultLocation(self):
        "读默认地址"
        with open(const.DefaultLocationPath, 'r') as f:
            self.ToDirname.set(f.readline())

    def special_getPasswordFromName(self):
        if askokcancel("警告", "命名格式符合标准的才可以读取,是否继续?"):
            name = os.path.split(os.path.splitext(self.From.get())[0])[-1]
            if len(name.split()) <= 3:
                showinfo("警告", "命名不符合标准格式，可能被改动或不是本程序产生")
            else:
                checkStr = name.split()[-3]
                if not checkModel.judgeCheckStr(checkStr):
                    showinfo("警告", "命名不符合标准格式，可能被改动或不是本程序产生")
                else:
                    p1, p2 = name.split()[-2:]
                    self.password1.set(p1)
                    self.password2.set(p2)
                    showinfo("提示", "更新密码成功")

    def setPasswordBoxValue(self):
        self.cbox['values'] = (
            "选择存储的密码", *list(
                map(lambda o: f"name=\"{o[0]}\": {o[1].password1} {o[1].password2}",
                    self.passwordDict.items())))

    def retPassword(self, *args):
        "从cbox处获得password并set"
        if self.cbox.current() > 0:
            s = self.passwordDict[tuple(self.passwordDict.keys())[
                self.cbox.current()-1]]
            self.password1.set(s.password1)
            self.password2.set(s.password2)

    def submit(self):
        """
        检验:
            密码不能有空格,有的话替换成_

        """
        ret = self.checkPasswordNULL()
        if ret != None:
            showinfo(title="警告", message=ret)
            return
        if not self.checkPasswordSpace_change():
            showinfo(
                title="警告", message="密码中含有空格，已自动替换成'_'")
            return
        ret = self.checkFrom()
        if ret != None:
            showinfo(title="警告", message=ret)
            return
        ret = self.checkTo()
        if ret != None:
            showinfo(title="警告", message=ret)
            return
        print(
            f" submit _compress {(self.From.get(),self.ToDirname.get(),self.ToFilename.get())}")
        succeed, ret = DeCM.DeCompress().work(
            self.From.get(), self.ToDirname.get(),
            self.ToFilename.get(), self.password1.get(), self.password2.get())
        if succeed:
            if succeed:
                print(getStrOfFilePath(ret))
                openFileInOS(ret)
        else:
            showinfo("error", ret)

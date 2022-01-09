from tkinter import *
from tkinter import font

from UI.view_CompressFrame import *
from UI.view_DeCompressFrame import *
from UI.view_OriginFrame import *
from UI.view_EditPasswordFrame import *
from UI.view_EditLocationFrame import *
from UI.view_InitFrame import *

from fileIO.fileIO import FlagJson


class MainPage:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry('600x550+500+240')

        self.page = Frame(self.root)
        self.page.pack()
        self.__initPage()
        self.__creatMenu()
        
        if FlagJson.getFirstOpen():
            self.openPage(self.OriginPage)
            self.__showFirstMessagebox()
            FlagJson.setFirstOpen(False)
        else:
            self.openPage(self.PageDict.get(FlagJson.getFirstPage(),self.OriginPage))

    def __creatMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(
            label="起始页", command=lambda: self.openPage(self.OriginPage))
        menubar.add_command(
            label="初始化", command=lambda: self.openPage(self.InitPage))

        editDefault = Menu(menubar, tearoff=False)
        editDefault.add_command(
            label="修改密码", command=lambda: self.openPage(self.EditPasswordPage))
        editDefault.add_command(
            label="修改地址", command=lambda: self.openPage(self.EditLocationPage))
        menubar.add_cascade(label="编辑", menu=editDefault)
        menubar.add_command(
            label="压缩", command=lambda: self.openPage(self.CompressPage))
        menubar.add_command(
            label="解压", command=lambda: self.openPage(self.DeCompressPage))
        menubar.add_command(label="Quit", command=self.root.quit)
        self.root['menu'] = menubar

    def __initPage(self):
        self.OriginPage = OriginFrame(self.root)
        self.InitPage = InitFrame(self.root)
        self.DeCompressPage = DeCompressFrame(self.root)
        self.CompressPage = CompressFrame(self.root)
        self.EditPasswordPage = EditPasswordFrame(self.root)
        self.EditLocationPage = EditLocationFrame(self.root)

        self.PageDict = {
            const.firstPageName_Origin: self.OriginPage,
            const.firstPageName_Init: self.InitPage,
            const.firstPageName_EditLocation: self.EditLocationPage,
            const.firstPageName_EditPassword: self.EditPasswordPage,
            const.firstPageName_Compress: self.CompressPage,
            const.firstPageName_DeCompress: self.DeCompressPage
        }

    def openPage(self, page):
        self.page.pack_forget()
        self.page = page
        self.page.pack()

    def __showFirstMessagebox(self):

        showinfo("欢迎",
                 """ 欢迎使用本程序
    教程和注意事项请看"起始页"
    "初始化"用于初始化程序的文件和结构
    "编辑"用于更改存储的默认信息
    "解压""压缩"是用于解压/压缩文件
    点击菜单上的按钮开始使用

    (本提示只会出现一次,使用愉快)
                                        --by PetterZ
""")

import os
from typing import Tuple

import constValue.comments as Comments
import constValue.constValue as const
import fileIO.fileStructure as fileStruct

import functionModel.checkModel as checkModel


def rar_compress(key, From: str, To: str, password: str = 'a123'):
    """
    key=1
        From: file or dict
        To  : dile(.rar)
    key=2
        From: file(.rar删除)
        To  : file(.zip)
    """
    fromPath = From
    toPath = To

    toPathDir = os.path.split(toPath)[0]
    if not os.path.exists(toPathDir):
        os.mkdir(toPathDir)

    command = f"rar a -ep1 -r -s -m3 -p{password} " if key == 1  \
        else f" WinRAR a -afzip -ep1  -r -s -m3 -dw -p{password} "

    ch = ' '.join([command, f"\"{toPath}\"", f"\"{fromPath}\""])

    print(ch)
    osRet = os.system(ch)
    print(f"system {osRet}")
    return osRet


def writeInfoToComments(path, comments):
    with open(path, 'w') as f:
        f.write(comments)


def rar_addComments(key, To, commentsPath):
    '''rar c -z"save2.txt" .\save2.rar"'''
    toPath = To
    command = f"rar c -z\"{commentsPath}\" " if key == 1  \
        else f" WinRAR c -z\"{commentsPath}\""
    ch = ' '.join([command, f"\"{toPath}\""])
    print(ch)
    osRet = os.system(ch)
    print(f"system {osRet}")
    return osRet


def ReName(from1Path: str) -> str:
    "添加后缀并返回"
    from2Path = from1Path+const.addName
    os.rename(from1Path, from2Path)
    return from2Path


def rar_Lock(key, To):
    "给rar/zip文件上锁"
    "winrar命令行上不了锁"
    toPath = To
    command = f"rar k " if key == 1  \
        else f" winrar k "
    ch = ' '.join([command, f"\"{toPath}\""])
    print(ch)
    osRet = os.system(ch)
    print(f"system {osRet}")
    return osRet


class Compress:
    def __init__(self) -> None:
        pass

    @staticmethod
    def work(From, ToDirname, ToFilename, password1, password2, checkStr) -> Tuple[bool, str]:
        "return true,to2Path  /  false,the_error"
        # abs处理,normpath处理
        workspaceName = fileStruct.getWorkspaceName()
        from1 = os.path.normpath(os.path.abspath(From))
        to1 = os.path.abspath(os.path.normpath(os.path.join(
            const.workspacePath, workspaceName, ToFilename+f' {password1}')+'.rar'))
        commentsPath=os.path.abspath(os.path.normpath(os.path.join(
            const.workspacePath, workspaceName+"comments")))
        # 压缩1
        if rar_compress(1, from1, to1, password1) not in const.go_no:
            print("压缩中发生错误，中断")
            return False, "压缩中发生错误，中断"

        # 加注释1
        writeInfoToComments(commentsPath,
                            Comments.creatcomments1(password1))
        rar_addComments(1, to1, commentsPath)

        # 上锁1
        rar_Lock(1, to1)

        print("the first Compress finish")
        # 重命名
        from2 = ReName(to1)

        to2 = os.path.join(
            ToDirname, ToFilename+f' {checkStr}'+f' {password1} {password2}'+'.zip')

        # 压缩2
        if rar_compress(2, from2, to2, password2) not in const.go_no:
            print("压缩中发生错误，中断")
            return False, "压缩中发生错误，中断"
        print("the second Compress finish")
        print(f"   to2 = {to2}")

        # 加注释2
        writeInfoToComments(commentsPath,
                            Comments.creatcomments2(password1, password2))
        rar_addComments(2, to2, commentsPath)

        # winrar上不了锁

        print("------------Succeed -----------")
        return True, to2


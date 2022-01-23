import os

import constValue.constValue as const
import fileIO.fileStructure as fileStruct

import fileIO.fileDel as fileDel

def rar_DeCompress(From: str, To: str, password: str = 'a123'):
    """
    key=1
        From: rar
        To  : dict
    key=2
        From: zip
        To  : dict
    """
    fromPath = From
    toPath = To
    command = f"winrar x -p{password} "

    ch = ' '.join([command, f"\"{fromPath}\"", f"\"{toPath}\""])

    print(ch)
    osRet = os.system(ch)
    print(f"system {osRet}")
    return osRet


def ReName(from1Path: str) -> str:
    "删除后缀并返回"
    # from2Path = from1Path[:-len(const.addName)]
    splitList=from1Path.split('.')
    splitList[-1]=splitList[-1].replace(const.addName,'')
    from2Path='.'.join(splitList)
    os.rename(from1Path, from2Path)
    return from2Path


class DeCompress:
    def __init__(self) -> None:
        pass

    @staticmethod
    def work(From, ToDirname, ToFilename, password1, password2) -> None:
        "return true,to2Path  /  false,the_error"
        workspaceName = fileStruct.getWorkspaceName()
        from1 = os.path.normpath(os.path.abspath(From))
        to1 = os.path.normpath(os.path.abspath(
            os.path.join(const.workspacePath, workspaceName)))+'\\'

        # 解压1
        if rar_DeCompress(from1, to1, password1) not in const.go_no:
            print("压缩中发生错误，中断")
            return False, "压缩中发生错误，中断"

        print("the first DeCompress finish")

        to2="NonePath"
        for f in os.listdir(to1):
            every = os.path.join(to1, f)
            if every.split('.')[-1] in  tuple(map(lambda x:x[1:]+const.addName,const.compressType))\
                or every.split('.')[-1] in tuple(map(lambda x:x[1:],const.compressType)):
                print(f"unrar -{every}")
                # 重命名
                from2 = ReName(every)

                to2 = os.path.normpath(os.path.join(
                    ToDirname, ToFilename, f.split('.')[0]))+'\\'

                # 压缩2
                if rar_DeCompress(from2, to2, password2) not in const.go_no:
                    print("压缩中发生错误，中断")
                    return False, "压缩中发生错误，中断"
                print("the second DeCompress finish  --|")
                print(f"   to2 = {to2}")

        fileDel.del_file(to1)

        print("------------Succeed -----------")
        return True, to2

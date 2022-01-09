import os
import shutil

import constValue.constValue as const
import fileIO.fileIO as fileIO
import fileIO.fileStructure as fileStruct
import constValue.readme as readme
import fileIO.fileDel as fileDel




def creatFolder(path):
    "建立文件夹"
    if not os.path.exists(path):
        os.mkdir(path)


def initFile(infoDict: dict, path: str):
    "根据fileStructure初始化文件"
    if 'initFunc' in infoDict.keys():
        infoDict['default']()
    else:
        fileIO.writeStrToFile(path, "")


def initFileStructure_AllFile():
    "初始化所有配置文件"
    def searchDFS(path, x):
        if type(x) == list:
            path = os.path.join(path, x[0])
            print(path)
            creatFolder(path)
            searchDFS(path, x[1])
        elif type(x) == tuple:
            for i in x:
                searchDFS(path, i)
        elif type(x) == dict:
            path = os.path.join(path, x['name'])
            initFile(x, path)
    searchDFS(".//", fileStruct.file_structure)


def initFileStructure_Dir():
    "初始化文件夹"
    def searchDFS(path, x):
        if type(x) == list:
            path = os.path.join(path, x[0])
            print(path)
            creatFolder(path)
            searchDFS(path, x[1])
        elif type(x) == tuple:
            for i in x:
                searchDFS(path, i)
        elif type(x) == dict:
            pass
    searchDFS(".//", fileStruct.file_structure)


def clear_workspace():
    "clear data_workspace"
    fileDel.del_file(const.workspacePath)


def clear_output():
    "clear data_output"
    fileDel.del_file(const.outputCompressPath)
    fileDel.del_file(const.outputDeCompressPath)


def initFile_readme():
    "初始化readme.txt"
    fileIO.writeStrToFile(const.readmePath,readme.readmeTxt)


def initFile_Location():
    "初始化Location.json"
    fileIO.LocationJson.pushLoactionDump_ToFile(
        const.DefaultLocationAll)


def initFile_Password():
    "初始化Password.json"
    fileIO.PasswordJson.pushPasswordDump_ToFile(
        const.DefaultPasswordJson)

def initFile_Flag():
    "初始化Flag.json"
    fileIO.FlagJson.pushFlagDump_ToFile(
        const.DefaultFlagJson)

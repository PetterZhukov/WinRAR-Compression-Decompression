import os

import fileIO.fileIO as fileIO
import fileIO.fileStructure as fileStructure


def creatFolder(path):
    "建立文件夹"
    if not os.path.exists(path):
        os.mkdir(path)


def initFile(infoDict: dict, path: str):
    "根据fileStructure初始化文件"
    if 'initFunc' in infoDict.keys():
        infoDict['initFunc']()
    else:
        fileIO.writeStrToFile(path, "")


def initFileStructure_AllFile():
    "初始化所有配置文件"
    def searchDFS(path, x):
        if type(x) == list:
            path = os.path.join(path, x[0])
            print(f"   search:{path}")
            creatFolder(path)
            searchDFS(path, x[1])
        elif type(x) == tuple:
            for i in x:
                searchDFS(path, i)
        elif type(x) == dict:
            path = os.path.join(path, x['name'])
            print(f"     init File:{path}")
            initFile(x, path)
    searchDFS(".//", fileStructure.file_structure)


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
    searchDFS(".//", fileStructure.file_structure)

import os
import constValue.constValue as const
from fileIO.fileIO import FlagJson, LocationJson, writeStrToFile
import constValue.readme as readme
import datetime

import functionModel.initModel as initModel
"""
文件夹 ["name",( 文件夹,文件   )]
文件  {"name":"" }
预定义的文件结构
"""
file_structure = ["",
                  (
                      {'name': 'readme.txt',
                       'initFunc': initModel.initFile_readme
                       },
                      ["data_Default",
                       (
                           {'name': 'Location.txt',
                            'initFunc': initModel.initFile_Location
                            },
                           {'name': 'Password.json',
                               'initFunc': initModel.initFile_Password
                            },
                           {'name': 'Flag.json',
                            'initFunc': initModel.initFile_Flag
                            }
                       )
                       ],
                      ["data_workspace",
                       ()
                       ],
                      ["data_output",
                       ()
                       ],
                  )
                  ]


def getWorkspaceName() -> str:
    """
    根据当前时间返回一个文件夹的名字
    e.g. 'time_2022_01_05_03:08:37'
    """
    t = datetime.datetime.now()
    return f"time_{t.year}_{t.month:>02}_{t.day:>02}__{t.hour:>02}_{t.minute:>02}_{t.second:>02}"


def getStrOfFilePath(path: str) -> str:
    "将一个路径处理成多层字符串"
    ret = ''
    space = '  '
    for i in path.split('\\'):
        ret += (space+'|--'+i+'\n')
        space += ' '
    return ret


def openFileInOS(path):
    "资源管理器中打开文件所在文件夹并选择"
    path = os.path.realpath(path)
    print(path)
    os.system(f'explorer /select, \"{path}\"')

def openFile(path):
    "直接打开文件"
    import subprocess as sp
    programName = "notepad.exe"
    fileName = path
    sp.Popen([programName, fileName])

if __name__ == '__main__':
    def searchDFS(path, x):
        if type(x) == list:
            path = os.path.join(x[0])
            print(path)
            searchDFS(path, x[1])
        elif type(x) == tuple:
            for i in x:
                searchDFS(path, i)
        elif type(x) == dict:
            print(f"{path}   {x['name']}")

    searchDFS("", file_structure)

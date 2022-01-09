import os
import shutil

import constValue.constValue as const
import fileIO.fileIO as fileIO
import constValue.readme as readme
import fileIO.fileDel as fileDel

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

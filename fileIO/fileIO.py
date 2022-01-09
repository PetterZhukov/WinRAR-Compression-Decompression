"""
    文件交互
"""

import json
from classDesign.password import password
import constValue.constValue as const


def initJson_File(path: str, to):
    "普通对象初始化json文件"
    with open(const.PasswordJsonPath, 'w', encoding='utf-8') as f:
        json.dump(to, f)


def writeStrToFile(path: str, to: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(to)


class PasswordJson:
    def __init__(self) -> None:
        pass

    @staticmethod
    def jsonToObject(s: dict):
        "json的dict -> class PasswordJson"
        if "__name__" in s and s["__name__"] == "password":
            return password(s['name'], s['password1'], s['password2'])
        return s

    @staticmethod
    def getPasswordLoad_byFile() -> dict:
        "get JsonFile Load"
        with open(const.PasswordJsonPath, 'r', encoding='utf-8') as f:
            return json.load(f, object_hook=PasswordJson.jsonToObject)

    @staticmethod
    def getPasswordLoad_byStr(s: str) -> dict:
        "get JsonStr Loads"
        return json.loads(s, object_hook=PasswordJson.jsonToObject)

    @staticmethod
    def getPasswordDump_byObject(to: list) -> str:
        "get object dumps to JsonStr"
        return json.dumps({o.name: o for o in to}, default=lambda o: o.__dict__)

    @staticmethod
    def pushPasswordDump_ToFile(to: list) -> None:
        "write object dump to File"
        with open(const.PasswordJsonPath, 'w', encoding='utf-8') as f:
            json.dump({o.name: o for o in to}, f, default=lambda o: o.__dict__)


class FlagJson:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getFlagLoad_byFile() -> dict:
        "get JsonFile Load"
        with open(const.FlagPath, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def pushFlagDump_ToFile(to: dict) -> None:
        "write object dump to File"
        with open(const.FlagPath, 'w', encoding='utf-8') as f:
            json.dump(to, f)

    @staticmethod
    def getFirstOpen() -> bool:
        "ret Flag.FirstOpen"
        return FlagJson.getFlagLoad_byFile().get(const.flag_firstOpenName, False)

    @staticmethod
    def setFirstOpen(v: bool) -> None:
        "set Flag.FirstOpen"
        flag = FlagJson.getFlagLoad_byFile()
        flag[const.flag_firstOpenName] = v
        FlagJson.pushFlagDump_ToFile(flag)

    @staticmethod
    def getFirstPage() -> str:
        "get Flag.FirstPage"
        return FlagJson.getFlagLoad_byFile().get(const.flag_firstPageName, const.firstPageName_Compress)

    @staticmethod
    def setFirstPage(v: str) -> None:
        "set Flag.FirstPage"
        flag = FlagJson.getFlagLoad_byFile()
        flag[const.flag_firstPageName] = v
        FlagJson.pushFlagDump_ToFile(flag)


class LocationJson:
    def __init__(self) -> None:
        pass

    @staticmethod
    def pushLoactionDump_ToFile(to: dict) -> None:
        "write object dump to File"
        with open(const.LoactionJsonPath, 'w', encoding='utf-8') as f:
            json.dump(to, f)

    @staticmethod
    def getLocationLoad_byFile() -> dict:
        "get JsonFile Load"
        with open(const.LoactionJsonPath, 'r', encoding='utf-8') as f:
            return json.load(f)

    #CompressFrom
    @staticmethod
    def getCompressFrom() -> dict:
        "get CompressFrom"
        return LocationJson.getLocationLoad_byFile().get(
            const.Location_CompressFromName, const.DefaultLocation_CompressFrom)

    @staticmethod
    def setCompressFrom(v:dict):
        "set [CompressFrom] = v"
        Location=LocationJson.getLocationLoad_byFile()
        Location[const.Location_CompressFromName]=v
        LocationJson.pushLoactionDump_ToFile(Location)
    
    #CompressTo
    @staticmethod
    def getCompressTo() -> dict:
        "get CompressTo"
        return LocationJson.getLocationLoad_byFile().get(
            const.Location_CompressToName, const.DefaultLocation_CompressTo)

    @staticmethod
    def setCompressTo(v:dict):
        "set [CompressTo] = v"
        Location=LocationJson.getLocationLoad_byFile()
        Location[const.Location_CompressToName]=v
        LocationJson.pushLoactionDump_ToFile(Location)

    #DeCompressTo
    @staticmethod
    def getDeCompressTo() -> dict:
        "get DeCompressTo"
        return LocationJson.getLocationLoad_byFile().get(
            const.Location_DeCompressToName, const.DefaultLocation_DeCompressTo)

    @staticmethod
    def setDeCompressFrom(v:dict):
        "set [DeCompressTo] = v"
        Location=LocationJson.getLocationLoad_byFile()
        Location[const.Location_DeCompressToName]=v
        LocationJson.pushLoactionDump_ToFile(Location)
















    @staticmethod
    def getLocationDefault() -> str:
        "获得 default location"
        return LocationJson.getLocationLoad_byFile().get(const.Location_defaultName, "")

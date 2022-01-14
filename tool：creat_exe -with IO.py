import os
import sys
from sys import exit
from shutil import copyfile
import shutil
import getopt
introduce = \
"""
    # 参数:      0 程序的运行地址
    #          -i  开启IO模式
    #             否则 用命令行运行
    #          --from 待打包的程序
    #          --to 打包的位置
    #          --intro 介绍
"""
# const
icoPath = "C:\\Users\\Zhukov\\Pictures\\B站头像3.ico"


print("开启IO模式")
if False:
    fromPath = os.path.abspath(input("  待打包的程序的位置\n     "))
    toPath = os.path.abspath(input("  打包的位置\n     "))
    print(fromPath + '\n' + toPath)
else:
    fromPath = os.path.abspath(r"C:\Users\Zhukov\Desktop\Code\VS Code\日常用 py\python解压zip\py_code\model-码云\winrar-compress-decompression\main.py")
    toPath=os.path.abspath(r"C:\Users\Zhukov\Desktop\Code\VS Code\日常用 py\python解压zip\py_code\model-码云\Exe-temp")


# exit
# 检查文件后缀
if os.path.splitext(fromPath)[1] != ".py":
    print("  文件后缀错误")
    exit()
# exit
# 检查py文件存在
if not os.path.exists(fromPath) or not os.path.exists(toPath):
    print("  py文件不存在")
    exit()

# 3个重要变量
# 运行pyinstaller位置
dirname, x=os.path.split(os.path.abspath(sys.argv[0]))
# 文件名
filename=os.path.splitext(os.path.split(fromPath)[1])[0]
# py文件位置
pyfilePath=fromPath

if False:
    # debug -print
    print(f"""
        {dirname}
        {filename}
        {pyfilePath}
        """)
# -i "{icoPath}"
if True:
    "make exe"
    system_name=f""" cd {dirname} && pyinstaller -i "{icoPath}" -F -w  "{pyfilePath}"       """
    print("\n\n\n" + system_name + "\n\n\n")
    os.system(system_name)

    "copy"
    source=f'{dirname}\\dist\\{filename}.exe'
    target=f'{toPath}\\{filename}.exe'

    print(source, '\n', target)
    copyfile(source, target)

    "delete"
    os.remove(f"{dirname}\\{filename}.spec")
    shutil.rmtree(f"{dirname}\\dist")
    shutil.rmtree(f"{dirname}\\build")
    shutil.rmtree(f"{os.path.split(fromPath)[0]}\\__pycache__")

    print("\n\n -----------------Creat Successfully \n\n")

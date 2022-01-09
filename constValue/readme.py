readmeTxt = """
================================================
        
        By PetterZHU
                    \(^o^)/~
                    
================================================
    本程序功能: 
        将一个文件/文件夹打包成一个双层压缩且带密码的压缩包
        将一个双层压缩的压缩文件解压到对应的位置
        且提供自定义快捷路径、密码等设置的功能

    注意事项:
    1. 程序基于rar软件，务必保证安装winRar程序且将其添加到环境变量
    2. 最好在初始页面点击按钮确认是否配置好path环境，不然出错后果自负owo

    初始化界面:
        查看是否配置好path环境，若成功会弹出winrar的界面以及显示弹窗
        更改默认文件解压到的路径
    
    压缩:
        从将文件/文件夹 压缩成为一个二次压缩的文件
        文件名: 设定好的文件名+校验码+第一层密码(内层)+第二层密码(外层)
        注意:
            密码不能有空格

    解压:
        将一个二次压缩的压缩包解压到某文件夹
        假如是本程序解压的文件，可以通过文件名的特殊格式来设置文件名和解压密码
    
    设置:
        可以增加和删除自定义快捷路径、密码等设置

    --注意:
        添加设置时若名字栏留空则会自动添加名字
        改完设置后压缩和解压两个窗口处需要点击"刷新"键来进行刷新,下拉框才会更新

    

"""

originTips="""
Tips:
    教程和注意事项请看"起始页"
    "初始化"用于初始化程序的文件和结构
    "编辑"用于更改存储的默认信息
    "解压""压缩"是用于解压/压缩文件
     
"""
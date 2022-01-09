from os.path import join
from classDesign.password import password
"结构"
"default dir"
DefaultPath = './/data_Default//'
LoactionJsonPath = join(DefaultPath, 'Location.json')
PasswordJsonPath = join(DefaultPath, "Password.json")
FlagPath = join(DefaultPath, "Flag.json")

"workspace dir"
workspacePath = './/data_workspace//'
"output dir  --存储解压解压和压缩结果"
outputPath = './/data_output//'
outputCompressPath=join(outputPath,'Compress//')
outputDeCompressPath=join(outputPath,'DeCompress//')
"read me"
readmePath = ".//readme.txt"

"json"
"json_password"
"       value"
password_defulatName = "Default"
"json_flag"
flag_firstOpenName = "FirstOpen"
flag_firstPageName = "FirstPage"
"       value"
firstPageName_Origin = "OriginPage"
firstPageName_Init = "InitPage"
firstPageName_EditLocation = "EditLocationPage"
firstPageName_EditPassword = "EditPasswordPage"
firstPageName_Compress = "CompressPage"
firstPageName_DeCompress = "DeCompressPage"
"json_Location"
Location_CompressFromName = "CompressFrom"
Location_CompressToName = "CompressTo"
Location_DeCompressFromName = "DeCompressFrom"
Location_DeCompressToName = "DeCompressTo"
"       value"
Location_defaultName = "Default"


"默认 select_fileStructure"
"   默认地址"
DefaultLocation_CompressFrom = {Location_defaultName:outputDeCompressPath}
DefaultLocation_CompressTo = {Location_defaultName:outputCompressPath}
DefaultLocation_CompressFrom = DefaultLocation_CompressTo
DefaultLocation_CompressFrom = {Location_defaultName:outputDeCompressPath}
"   默认密码"
DefaultPasswordJson = [password(password_defulatName, "a123", "a123")]
"   默认flag"
DefaultFlagJson = {flag_firstOpenName: True,
                   flag_firstPageName: firstPageName_Compress}

'密码中的空格'
"""
    ' '->'_'
"""

'添加的后缀'
addName = '删除'

"winrar返回值判断表"
go_no = (0, 1)


"用于字符串哈希的素数"
"校验码格式   check_aaa_bbb"
hash_list = [1, 11, 37]
hash_figure = 2       # 生成码的位数
breakSymbol = '_'     # 分隔符
checkSign = "Check"

"解压压缩文件的后缀"
compressType = ('.rar', '.zip', '.7z')
filetypes_speial = (('压缩格式1', compressType),)

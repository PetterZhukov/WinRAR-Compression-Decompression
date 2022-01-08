# 程序问题 -bug
- [x] 地址到底是相对还是绝对
- [pass] 两个版本，一个版本可以有输入框，一个地址只由框选择来选定
- [pass] To ->同文件夹
- [x] 校验码 -> Check_xxx_xxx
- [x] 密码中不能有空格
- [x] 解压处预览文件夹位置也要改，关于zip的
- [x] gitignore
- [ ] 持续更新init
- [x] 消除测试数据
- [x] git更新日志文件 gitignore
- [x] 整理日志
- [ ] system('pause') 到时候去掉(显示命令行则保留，去掉命令行则去掉)
- [ ] 显示/不显示命令行
- [ ] 设置addName
- [ ] 根据后缀前面几个字智能判断文件类型
- [ ] 初始页面 init workspace
- [ ] 使用github上传
- [ ] git删除大文件
- [ ] 总体使用一遍git
- [ ] 更改为下拉框选择默认路径，json结构 -> ttk , 文件存储,constValue
- [ ] 写产生文件树的函数,更新结构.txt
- [ ] 增加功能v4
    - [ ] 初始提示页面
    - [ ] 初始化/增加/删除 设置
    - [ ] 设置打开的时候开始哪个页面   -Flag.json
    - [ ] 自定义Location            -Loctaion.json
    - [ ] 自定义内外层压缩格式
    - [ ] 是否产生命令行
    - [ ] 读写交互放在单独的文件夹里面
    - [ ] 调包规范化
    - [ ] 有的showinfo改成showerror,showwarning    https://www.cnblogs.com/buchizaodian/p/7076964.html
    - [ ] 除去mainpage的注释
    - [ ] 除去origin的注释
    - [ ] 重写 compress和decompress
    - [ ] 修改 FirstPage
    - [ ] 补上comments

# 注意事项
 - [ ] 更新init
 - [ ] 下拉框的0要排除掉
   - [ ] 下拉框的1不能删除

# 设计优化方向    
- [x] 用normpath增强鲁棒性
- [ ] 简化normpath、abspath
- [ ] 根据默认存储确认是否已经初始化来确定是否出现起始页
备忘录
- [ ] 广义版本:
    - [ ] 根据内外层判断，可以用文件存储特定实现快速设置
- [ ] 存储密码、第1.2.层的后缀
- [x] 狭义版本:
    - [x] 根据check核定然后直接解压zip - rar
- [x] 文件名不变会增加1,2,3.......
- [x] abs挪到前面
- [x] 清空工作区
- [x] init函数还未实装
    - [x] init文件结构
    - [x] init workspace
- [x] 每次workspace根据日期创建文件夹避免串线
- [x] ui返回结果
- [x] 解压完删除第一次解压的结果
- [x] 标题
- [x] 7Z ->
- [ ] pysimplegui
- [ ] ctrl+单击 跳转代码
- [ ] 

    
# 暂时用不上的功能：
- [ ] 分卷功能
- [ ] rar,winrar 加注释

- [ ] 用xml更改数据存储

- [ ] 优化ui


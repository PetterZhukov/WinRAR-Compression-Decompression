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
- [x] 初始页面 init workspace
- [x] 使用github上传  -> 码云
- [x] git删除大文件 -> 直接把.git删了
- [ ] 总体使用一遍git
- [x] 更改为下拉框选择默认路径，json结构 -> ttk , 文件存储,constValue
- [x] 写产生文件树的函数,更新结构.txt
- [ ] 增加功能v4
    - [x] 初始提示页面
    - [x] 初始化/增加/删除 设置
    - [x] 设置打开的时候开始哪个页面   -Flag.json
    - [x] 自定义Location            -Loctaion.json
    - [ ] 自定义内外层压缩格式
    - [ ] 是否产生命令行
    - [x] 读写交互放在单独的文件夹里面
    - [x] 调包规范化
    - [x] 有的showinfo改成showerror,showwarning    https://www.cnblogs.com/buchizaodian/p/7076964.html
    - [x] showerror和showwarning选择哪个 -> 警告 和 报错
    - [x] 除去mainpage的注释
    - [x] 除去origin的注释
    - [x] 重写 compress和decompress
    - [x] 修改 FirstPage
    - [x] 补上comments
    - [x] 重新读写json要刷新其他读取json的页面 ->手动刷新 / 每次打开都自动刷新
    - [x] Location分为 CompressFrom,CompressTo,DeCompressTo
    - [ ] 修改路径/密码的条得可编辑且够长够宽
    - [x] 保护default
    - [x] data_output分为解压和压缩
    - [x] 修改flag
    - [x] password 也先更新json然后从json拿取
    - [x] 压缩到的路径应该是Compress
    - [x] Decompress也需要分可视化get
    - [x] Compress 默认位置失灵
    - [x] 调整页面大小
    - [x] 优化import结构（太乱）
    - [x] current(0) password 多了
    - [x] 修改提示"选择存储的路径"
    - [pass] origin先运行，然后要运行的时候才创建其他部分，保证安全
    - [x] 单独的初始化小程序
    - [x] DeCompress的cbox名字改成passwordCBox
    - [x] init 界面添加readme
    - [x] 解压预览适配
    - [x] 解压第二个文件名用replace
    - [ ] 自定义后缀
    - [ ] exe版本压缩报错
    - [ ] 鼠标放上去的时候显示提示
- [ ] 码云的拉取失败了，怎么以本地为主创建仓库
- [ ] 整理test文件夹

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


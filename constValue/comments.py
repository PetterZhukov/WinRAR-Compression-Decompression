import constValue.constValue as const


def creatcomments2(pasword1, password2):
    return \
        f'''这个文件使用双层压缩，
    内层密码是{pasword1},
    外层密码是{password2},
    解压一次以后需要删除后缀的'{const.addName}'
'''


def creatcomments1(pasword1):
    return \
        f'''这个文件密码是{pasword1}
'''

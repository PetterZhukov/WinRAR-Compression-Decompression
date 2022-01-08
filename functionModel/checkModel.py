import random
import constValue.constValue as const


def creatRandomN() -> int:
    "产生hash_figure位的随机数"
    return random.randint(10**(const.hash_figure-1), 10**(const.hash_figure)-1)


def splitCheckStr(inStr: str) -> tuple:
    " 'xxxx_aaa_bbb' -> [aaa,bbb]"
    a, b = map(int, (inStr.split(const.breakSymbol)[1:3]))
    return a, b


def judgeCheckStr(inStr: str)->bool:
    "根据字符串判断正误"
    x, y = splitCheckStr(inStr)
    if getHash(x) == y:
        return True
    else:
        return False


def getHash(x: int) -> int:
    "获取哈希值"
    sum = 0
    for i in (const.hash_list):
        sum += i*(x % 10)
        x //= 10
    return sum


def creatCheckStr() -> str:
    "产生验证字符串"
    orgin = creatRandomN()
    return const.breakSymbol.join((const.checkSign, str(orgin), str(getHash(orgin))))


if __name__ == '__main__':
    print(creatCheckStr())
    print(judgeCheckStr("Check_865_367"))

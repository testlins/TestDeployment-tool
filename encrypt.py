#coding=utf-8
import random

class jiajiemi(object):
    """密码自定义加解密"""
    def __init__(self, char, headkey='k', key='x'):
        super(jiajiemi, self).__init__()
        self.char = char #待加密字符串
        self.headkey = headkey #加密头key 默认为k
        self.key = key #加密部key 默认为x
        
    def jiami(self):
        char = self.char
        headkey = self.headkey
        key = self.key
        randomkey = random.randint(0,255)
        jiamichar =hex(randomkey^ord(headkey))#ord 函数为将字母转换为asc数字 hex为生成十六进制数；这里计算加密头
        for item in char:#循环加密
            jiamichar += hex(ord(key)^ord(item)^randomkey)[-2:]#去掉重复0x
        return jiamichar

    def jiemi(self,jiamichar):
        headkey = self.headkey
        key = self.key
        char = ''
        randomkey = ord(headkey)^int(jiamichar[2:4], 16) 
        for i in xrange(4, len(jiamichar)-1, 2):
            char += chr(randomkey^ord(key)^int(jiamichar[i:i+2], 16))#int(x, 16)为转换字符串为10进制数，chr函数转换asc码为字母
        return char

if __name__ == '__main__':
    a = jiajiemi('test','t')
    print a.jiami()
    print a.jiemi('0xe79f8e989f')

# _*_ coding:UTF-8 _*_
# b64 decode and encode

import base64


def b32encode(string):
    a = base64.b32encode(string.encode())
    return a.decode()


def b32decode(string):
    try:
        a = base64.b32decode(string).decode("utf8", "ignore")
    except:
        a="客官您的数据格式不像是base32的密文鸭 多半是凉了 抱歉哦(⊙o⊙) 或者您换个加密方式"
    return a

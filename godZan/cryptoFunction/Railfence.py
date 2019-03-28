# _*_ coding=UTF-8 _*_

from pycipher import Railfence


def Rail_encode(e, f):
    elen = len(e)
    b = elen / f
    result = {x: '' for x in range(int(b))}
    for i in range(elen):
        a = i % b;
        result.update({a: result[a] + e[i]})
    d = ''
    for i in range(int(b)):
        d = d + result[i]
    return d;


def Rail_brute(string):
    output=""
    elen = len(string)
    field = []  # field 为所有可能的栏数
    for i in range(2, elen):
        if (elen % i == 0):
            field.append(i)
    for f in field:
        output=output+"f:"+str(f)+" "+str(Rail_encode(string, f))+"\n"
    return output
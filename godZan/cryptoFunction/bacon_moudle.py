# coding:utf8

import re

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

first_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"]

second_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","baabb","babaa","babab","babba","babbb"]

def encode(s):
    upper_flag = False # 用于判断输入是否为大写
    string = s
    if string.isupper():
        upper_flag = True
        string = string.lower()
    e_string1 = ""
    e_string2 = ""
    for index in string:
        for i in range(0,26):
            if index == alphabet[i]:
                e_string1 += first_cipher[i]+" "
                e_string2 += second_cipher[i]+" "
                break
    if upper_flag:
        e_string1 = e_string1.upper()
        e_string2 = e_string2.upper()
    output="第一种加密方式密文为 "+e_string1+"\n"+"第二种加密方式密文为 "+e_string2
    return output


def decode(s):
    upper_flag = False  # 用于判断输入是否为大写
    e_string = s.replace(' ','')
    if e_string.isupper():
        upper_flag = True
        e_string = e_string.lower()
    e_array = re.findall(".{5}",e_string)
    d_string1 = ""
    d_string2 = ""
    for index in e_array:
        for i in range(0,26):
            if index == first_cipher[i]:
                d_string1 += alphabet[i]
            if index == second_cipher[i]:
                d_string2 += alphabet[i]
    if upper_flag:
        d_string1 = d_string1.upper()
        d_string2 = d_string2.upper()
    output="第一种加密方式明文为 "+d_string1+"\n"+"第二种加密方式明文为 "+d_string2
    return output


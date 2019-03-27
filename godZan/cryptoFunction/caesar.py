# _*_ coding:UTF-8 _*_

from pycipher import Caesar

# 加密 向后移
def caesar_decode(string, key):
    plaintext = Caesar(int(key)).decipher(string, keep_punct=True)
    return plaintext

# 解密 向前移
def caesar_encode(string, key):
    plaintext = Caesar(int(key)).encipher(string, keep_punct=True)
    return plaintext

# 爆破
def caesar_brute(string):
    for i in range(26):
        print('%s:'% i, end='')
        a = caesar_encode(string, i)
        print(a)

def kaisa(lstr):
	count=0
	returnStr=""
	for p in range(127):
		str1 = ''
		for i in lstr:
			temp = chr((ord(i)+p)%127)
			if 32<ord(temp)<127 :
				str1 = str1 + temp
				feel = 1
			else:
				feel = 0
				break
		if feel == 1:
			count=count+1
			returnStr = returnStr + str(count)+":"+str1 + '\n'
	return returnStr



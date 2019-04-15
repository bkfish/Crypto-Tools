import binascii
from django.http import JsonResponse
from django.http import HttpResponse
from cryptoFunction import  commode_moudle,moder_moudle,bacon_moudle,b64_moudle,b58_moudle,b32_moudle,b16_moudle,caesar_moudle,Railfence
# Create your views here
from cryptoFunction.morse_moudle import Morse
import urllib.request
from django.shortcuts import render_to_response, render, redirect
from cryptoFunction.jsfuck_moudle import JSFuck
from pycipher import Autokey
from pycipher import Vigenere

#BASE家族
def base(request):
    if request.method=='POST':
        input = request.POST['input']
        type=request.POST['type']
        if type=="b64e":
            output = b64_moudle.b64encode(input)
        elif type =="b64d":
            output = b64_moudle.b64decode(input)
        elif type=="b32e":
            output = b32_moudle.b32encode(input)
        elif type =="b32d":
            output = b32_moudle.b32decode(input)
        elif type=="b16e":
            output = b16_moudle.b16encode(input)
        elif type =="b16d":
            output = b16_moudle.b16decode(input)
        elif type=="b58e":
            output = b58_moudle.b58encode(input)
        elif type =="b58d":
            output = b58_moudle.b58decode(input)
        else :
            output="客官鸭 你这是什么操作??"
        return HttpResponse(output)
    else:
        return render(request, 'base.html',{'output':"",'input':''})

#Hex编码
def hexAscii(request):
    if request.method=='POST':
        input = request.POST['input']
        input=input.encode()
        type=request.POST['type']
        if type=="hex":
            try:
                output = binascii.a2b_hex(input)
            except:
                output = "客官您的数据格式不像是十六进制的密文鸭 多半是凉了 抱歉哦(⊙o⊙) 或者您换个加密方式"
        elif type == "ascii":
            output = binascii.b2a_hex(input)
        else:
            output = "客官鸭 你这是什么操作??"
        return HttpResponse(output)
    else:
        return render(request, 'hexAscii.html', {'output': "", 'input': ''})

#URL编码
def urlCode(request):
    if request.method=='POST':
        input = request.POST['input']
        type=request.POST['type']
        if type=="encode":
            output=urllib.request.quote(input,encoding='UTF-8')
        elif type == "decode":
            output = urllib.request.unquote(input, encoding='UTF-8')
        else:
            output = "客官鸭 你这是什么操作??"
        return HttpResponse(output)
    else:
        return render(request, 'urlCode.html', {'output': "", 'input': ''})

#莫斯编码
def morse(request):
    if request.method=='POST':
        input = request.POST['input']
        type=request.POST['type']
        output=''
        if type=="encode":
            a = Morse()
            b = a.morse_en(input)
            for i in b:
                output=output+i+' '
        elif type == "decode":
            a = Morse()
            b = a.morse_de(input)
            for i in b:
                output = output + i + ' '
            if output == '':
                output = "客官鸭 您确定您是摩尔斯密码?? 建议您先随意加密一下学习一下摩尔斯密码格式"
        else:
            output = "客官鸭 你这是什么操作??"
        return HttpResponse(output)
    else:
        return render(request, 'morse.html', {'output': "", 'input': ''})

#莫斯表
def morseTable(request):
    return render(request, 'morseTable.html')

#进制转化
def converter(request):
    if request.method=='POST':
        input = request.POST['input']
        type=request.POST['type']
        output = {"binOutput":"","octOutput":"","decOutput":"","hexOutput":""}
        try:
            if type=="bin":
                output["binOutput"]="0b"+input
                dec=int(input,2) # 拿到了十进制
                output["octOutput"]=str(oct(dec)) #八进制
                output["decOutput"]="0d"+str(dec) #十进制
                output["hexOutput"]=str(hex(dec)) #十六进制
            elif type == "oct":
                dec=int(input,8) # 拿到了十进制
                output["binOutput"]=str(bin(dec)) #二进制
                output["octOutput"]=str(oct(dec)) #八进制
                output["decOutput"]="0d"+str(dec) #十进制
                output["hexOutput"]=str(hex(dec)) #十六进制
            elif type == "dec":
                dec=int(input,10) # 拿到了十进制
                output["binOutput"]=str(bin(dec)) #二进制
                output["octOutput"]=str(oct(dec)) #八进制
                output["decOutput"]="0d"+str(dec) #十进制
                output["hexOutput"]=str(hex(dec)) #十六进制
            elif type == "hex":
                dec=int(input,16) # 拿到了十进制
                output["binOutput"]=str(bin(dec)) #二进制
                output["octOutput"]=str(oct(dec)) #八进制
                output["decOutput"]="0d"+str(dec) #十进制
                output["hexOutput"]=str(hex(dec)) #十六进制
            else:
                output["binOutput"]=output["octOutput"]=output["decOutput"]=output["hexOutput"]="客官您输入错误"
        except:
            output["binOutput"]=output["octOutput"]=output["decOutput"]=output["hexOutput"]="客官您确定格式对啦??小站顶不住啦啦，或者您选择转换方式不对？？"
        return JsonResponse(output)
    else:
        return render(request, 'converter.html')

#凯撒
def caesar(request):
    if request.method=='POST':
        key=request.POST['key']
        input = request.POST['input']
        type=request.POST['type']
        output =""
        if type=="caencode":
            output=caesar_moudle.caesar_encode(input, key)
        elif type=="cadecode":
            output=caesar_moudle.caesar_decode(input, key)
        elif type=="cabrute":
            output=caesar_moudle.caesar_brute(input)
        elif type=="kaisa":
            output=caesar_moudle.kaisa(input)
        else:
            output="客官您是什么操作呀？？"
        return HttpResponse(output)
    else:
        return render(request, 'caesar.html')

#栅栏解密
def fence(request):
    if request.method=='POST':
        key=request.POST['key']
        input = request.POST['input']
        type=request.POST['type']
        output =""
        try:
            if type=="encode":
                output=Railfence.Rail_encode(input,int(key))
            elif type=="brute":
                output=Railfence.Rail_brute(input)
            else:
                output="客官您是什么操作呀？？小赞看不懂"
        except:
            output="小赞已崩，客官请谨慎输入鸭,您输入有误"
        return HttpResponse(output)
    else:
        return render(request, 'fence.html')

#培根
def bacon(request):
    if request.method=='POST':
        input = request.POST['input']
        type=request.POST['type']
        output =""
        try:
            if type=="encode":
                output=bacon_moudle.encode(input)
            elif type=="decode":
                output=bacon_moudle.decode(input)
            else:
                output="客官您是什么操作呀？？"
        except:
            output="小赞已崩，客官请谨慎输入鸭,您输入有误"
        return HttpResponse(output)
    else:
        return render(request, 'bacon.html')

#jsfuck
def jsfuck(request):
    if request.method=='POST':
        type=request.POST['type']
        input = request.POST['input']
        output =""
        if type=="evalencode":
            output=JSFuck(input,True).encode()
        elif type == "encode":
            output=JSFuck(input).encode()
        else :
            output="小赞已崩，客官请谨慎输入鸭,您输入有误"
        return HttpResponse(output)
    else:
        return render(request, 'jsfuck.html')

def rsa(request):
    return render(request,'rsa.html')

facoutput=""

#分解因数
def fac1(num):
  for i in range(2,num):
      global facoutput 
      if num % i == 0 :
          facoutput += str(i)+" * "
          fac1(num//i)
          return
  facoutput+=str(num)

def fac(request):
    global facoutput
    if request.method=='POST':
        input = request.POST['input']
        output =""
        num=int(input)
        fac1(num)
        output=facoutput
        return HttpResponse(output)
    else:
        return render(request,'fac.html')

#分解模数
def moder(request):
    if request.method=='POST':
        n = request.POST['inputN']
        e = request.POST['inputE']
        d= moder_moudle.get_rsa_e_d(int(n),int(e),None)
        output=str(d)
        return HttpResponse(output)
    else:
        return render(request,'moder.html')

#共模攻击
def commode(request):
    if request.method=='POST':
        n = request.POST['inputN']
        c1 = request.POST['inputC1']
        c2 = request.POST['inputC2']
        e1 = request.POST['inputE1']
        e2 = request.POST['inputE2']
        n=int(n)
        c1=int(c1)
        c2=int(c2)
        e1=int(e1)
        e2=int(e2)
        s = commode_moudle.egcd(e1,e2)
        s1 = s[1]
        s2 = s[2]
        # 求模反元素
        if s1 < 0:
            s1 = - s1
            c1 = commode_moudle.modinv(c1, n)
        elif s2 < 0:
            s2 = - s2
            c2 = commode_moudle.modinv(c2, n)
        m = (c1**s1)*(c2**s2) % n
        output=str(m)
        return HttpResponse(output)
    else:
        return render(request,'commode.html')

def vigenere(request):
    if request.method=='POST':
        key=request.POST['key']
        input = request.POST['input']
        type1=request.POST['type']
        output =""
        if key=='0':
            output="请输入Key??"
            return HttpResponse(output)
        if type1=="ve":
            output=Vigenere(key).encipher(input)
        elif type1=="vd":
            output=Vigenere(key).decipher(input)
        elif type1=="ae":
            output=Autokey(key).encipher(input)
        elif type1=="ad":
            output=Autokey(key).decipher(input)
        else:
            output="客官您是什么操作呀？？"
        return HttpResponse(output)
    else:
        return render(request, 'vigenere.html')

def rsascript(request):
    return render(request,'rsascript.html')

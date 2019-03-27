import binascii

from django.http import HttpResponse
from cryptoFunction import md5_moudle,b64_moudle,b58_moudle,b32_moudle,b16_moudle,caesar,Railfence,ascii_brute_moudle,rot13_moudle,RGB2pic_moudle,factorization_moudle,num_to_QR_moudle
# Create your views here
from cryptoFunction.morse_moudle import Morse
import urllib.request
from django.shortcuts import render_to_response, render, redirect

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

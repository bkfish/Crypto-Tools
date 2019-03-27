from django.http import HttpResponse
from cryptoFunction import md5_moudle,MD5_online_crack,b64_moudle,b58_moudle,b32_moudle,b16_moudle,caesar,Railfence,ascii_brute_moudle,rot13_moudle,RGB2pic_moudle,factorization_moudle,num_to_QR_moudle
# Create your views here.
import urllib.request
from django.shortcuts import render_to_response, render, redirect


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


from django.http import HttpResponse
from cryptoFunction import b64_moudle


# Create your views here.
from django.shortcuts import render_to_response, render




def index1(request):
    string = "flag"
    a = b64_moudle.b64encode(string)
    return HttpResponse(a)


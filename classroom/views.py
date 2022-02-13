from django.http import HttpRequest
from django.shortcuts import render

def hello(request:HttpRequest):
    return render(request,'index.html',context={"name":"pritam"})

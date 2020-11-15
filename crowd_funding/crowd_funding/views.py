from django.http import HttpResponse
from django.shortcuts import render

def start(request):
    cont={
        "msg":"hello team 2"
    }
    return HttpResponse("hello team 2")

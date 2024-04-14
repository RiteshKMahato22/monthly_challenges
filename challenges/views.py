from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def month1(request):
    return HttpResponse("This is January.")

def month2(request):
    return HttpResponse("This is February.")

def month3(request):
    return HttpResponse("This is March.")





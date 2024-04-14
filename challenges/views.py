from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

def monthly_challenge(request,text):
    url_text=None
    if text=="january":
        url_text="This is January."
    elif text=="february":
        url_text="This is february."
    elif text=="february":
        url_text="This is february."
    else:
        return HttpResponseNotFound("This month is not yet developed.")
    return HttpResponse(url_text)





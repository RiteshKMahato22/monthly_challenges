from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.

month_dict = {
    "january":"This is January",
    "february":"This is february",
    "march":"This is march",
    "april":"This is april",
    "may":"This is may",
    "june":"This is june",
    "july":"This is july",
    "august":"This is august",
    "september":"This is september",
    "october":"This is october",
    "november":"This is november",
    "december":"This is december"
}

def monthly_challenge(request,month):
    try:
        challenge_text=month_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("The month is not yet developed")

def monthly_challenge_by_number(request,month):
     months=list(month_dict.keys())
     try:
         redirect_month=months[month-1]
         return HttpResponseRedirect("/challenges/"+redirect_month)
     except:
        HttpResponseNotFound("Out of range")






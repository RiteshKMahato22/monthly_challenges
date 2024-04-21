from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

month_dict = {
    "january":"This is January",
    "february":"This is february",
    "march":"This is march",
    "april":"Hi folks! If you are reading this message, let me introduce myself - I am team ezykroot, we are building something special. Our motto is hiring made easy!!",
    "may":"This is may",
    "june":"This is june",
    "july":"This is july",
    "august":"This is august",
    "september":"This is september",
    "october":"This is october",
    "november":"This is november",
    "december":"This is december"
}

def challenges(request):
    lis=""
    months=list(month_dict.keys())
    for month in months:
        capitalised_months=month.capitalize()
        redirect_month=reverse("revname",args=[month])
        lis+=f"<li><a href=\"{redirect_month}\">{capitalised_months}</li>"
    response_data=f"<ul>{lis}</ul>"
    return HttpResponse(response_data)
def monthly_challenge(request,month):
    try:
        challenge_text=month_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("The month is not yet developed")

def monthly_challenge_by_number(request,month):
     months=list(month_dict.keys())

     try:
         redirect_month = months[month - 1]
         redirect_path = reverse("revname", args=[redirect_month])
         return HttpResponseRedirect(redirect_path)
     except:
         return HttpResponseNotFound("Out of range")






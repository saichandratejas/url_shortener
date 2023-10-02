from django.http import Http404
from django.shortcuts import redirect, render,HttpResponse
from .models import urlModel
import random

# Create your views here.
def home(request):
    return render(request,"landingPage.html")

def makeshorturl(request):
    if request.method=='POST':
        longurl=request.POST['longurl']
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$*&^%-+."
        shorturl=("".join(random.sample(s,6)))
        obj=urlModel.objects.create(longurl=longurl,shorturl=shorturl)
        print("Object created")
        shorturl="http://127.0.0.1:8000/"+shorturl
    #return HttpResponse("Your shorturl for {} is {}".format(longurl,shorturl))
    return render(request,"urlcreated.html",{"shorturl":shorturl,"longurl":longurl})

def redirecturl(request,shorturl):
    print(shorturl)
    try:
        obj=urlModel.objects.get(shorturl=shorturl)
    except urlModel.DoesNotExist:
        obj=None

    if obj is not None:
        print("Object Found")
        print(obj.longurl)
        obj.count+=1
        obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("Check your url")
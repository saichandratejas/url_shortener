from django.shortcuts import HttpResponse

def sample(request):
    return HttpResponse('<h1>Hello World</h1>')
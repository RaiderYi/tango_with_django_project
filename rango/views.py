from django.shortcuts import render

# Create your views here
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner!")


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request,'rango/index.html',context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Shijie Fang!"}
    return render(request,'rango/about.html',context=context_dict)
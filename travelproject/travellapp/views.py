from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Contact


def demo(request):
    obj = Place.objects.all()
    list1 = Contact.objects.all()
    return render(request,"index.html",{'result':obj,'rslt':list1})


    # name="python"
    return render(request,"index.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#
#     add=x+y
#     mult=x*y
#     sub=x-y
#     dev=x/y
#
#     return render(request,"result.html",{'addition':add,'multiplication':mult,'subtraction':sub,'division':dev})
# def contact(request):
#     return HttpResponse("hellooo world im python")

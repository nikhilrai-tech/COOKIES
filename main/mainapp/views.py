from urllib import response
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def set(request):
    response= render(request,'set.html')
    response.set_cookie("name","nikhil rai",max_age=60*60*24)
    response.set_cookie("email","nikhilrai662@gmail.com")
    return response


def get(request):
    name=request.COOKIES.get("name",None)
    email=request.COOKIES.get("email",None)
    return render(request,'get.html',{"Name":name,"Email":email})


def update(request):
    response= render(request,'update.html')
    response.set_cookie("name","amit",max_age=60*60*24)
    response.set_cookie("email","amit@gmail.com")
    return response

def delete(request):
    response= render(request,'delete.html')
    response.delete_cookie("name")
    response.delete_cookie("email")
    return response

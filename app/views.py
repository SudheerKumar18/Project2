from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def one(request):
    return HttpResponse('one is good')
def two(request):
    return HttpResponse('<h1>two is good</h1>')
def three(request):
    return HttpResponse('<i>three is good</i>')
from django.http import HttpResponse
def four(request):
    return HttpResponse("<img src='https://tse3.mm.bing.net/th?id=OIP.7ybCWV5tr4r4rAwadk2XUwHaEK&pid=Api&P=0&h=220' />")


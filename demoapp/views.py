from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    return HttpResponse('<h1>hello world</h1>')
# Create your views here.

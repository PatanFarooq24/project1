from django.shortcuts import render
from django.http import HttpResponse
def wish1(request):
    return HttpResponse('<h1>Hello</h1>')
# Create your views here.

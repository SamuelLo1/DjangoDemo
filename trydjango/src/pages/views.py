from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args, **kwargs): 
    resp = "<h1>Hello World</h1>"
    return HttpResponse(resp)
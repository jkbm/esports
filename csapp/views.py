from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def temp(request):

    return HttpResponse('Hello, world! This is CS GO part of the web-site')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_message(request):
    return_msg="Welcome to Django Session"
    return HttpResponse(return_msg)
    

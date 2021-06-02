from django.shortcuts import render
from django.http import HttpRespons

# Create your views here.
def show_message(request):
    return_msg="Welcome to Django Session"
    return HttpResponse(return_msg)
    
    
def realme(request):
    return_mobile='welcome to realme'
    return HttpResponse(return_mobile)
    
    
def aadhar(request):
    return_aadhar='welcom to aadhar'
    return HttpResponse(return_aadhar)
    
def voterid(request):
    return_voterid='welcome to voterid\n*****\n my voterid no 1234'
    return HttpResponse(return_voterid)
    
def pancard(request):
    return_pancard='welcome to pancard'
    return HttpResponse(return_pancard)


 

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bank_fun(request):
    message_bank='welcome to bank'
    return HttpResponse(message_bank)
    
def home(request):
    #return HttpResponse('Welcome to Homepage!!')
    return render(request,'homepage.html')
    
def blog(request):
    return render(request,'blog.html')

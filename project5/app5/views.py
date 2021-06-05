from django.shortcuts import render

# Create your views here.

def new_project(request):
    return render(request,'new_project.html')

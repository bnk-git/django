from django.shortcuts import render


# Create your views here.
def bank(request):
    return render(request,"project8.html")
    
##
def page(request):
    return render(request,"file1.html")
    
 ##new
def realme(request):
    return render(request,"file2.html")

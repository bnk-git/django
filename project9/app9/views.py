from django.shortcuts import render


# Create your views here.
def getdata(request):
    return render(request, "file1.html")

from django.shortcuts import render
from django.http import HttpResponse

def showindex(request):
    return render(request,"index.html")


def registeruser(request):

    f_name = str(request.POST.get("t1"))
    l_name = str(request.POST.get("t2"))

    #full_name = f_name+" "+l_name

    return render(request, 'index.html')





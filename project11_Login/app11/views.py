from django.shortcuts import render

# Create your views here.
def card(request):
    return render(request,"Login.html")

def logincheck(request):

    cardname  = request.POST.get("t1")
    password = request.POST.get("t2")
    if cardname == "bubunkar" and password == "Bubun@456":
        return render(request, 'welcome.html')
    else:
        return render(request, 'error.html')




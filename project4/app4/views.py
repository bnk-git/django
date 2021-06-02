from django.shortcuts import render

# Create your views here.
def stock_exchange(request):
    return render(request,"stock.html")

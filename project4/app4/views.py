from django.shortcuts import render

# Create your views here.
def stock_exchange(request):
    stock_details= { 'stock_name1': {'SBI': '400'},
                     'stock_name2': {'PNB': '45'}}
               
    data = {"my_stock":stock_details}
    
               
    return render(request,"stock.html",data)


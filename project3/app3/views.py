from django.shortcuts import render

# Create your views here.
def html_tag(request):
    return render(request, 'file.html')
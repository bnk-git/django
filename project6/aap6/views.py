from django.shortcuts import render

# Create your views here.
def employee(request):
    stock_details= employee_details = {"employee_name":"bubun", "employee_num":78765444, "employee_salary":20000}
    return render(request,"employee.html",employee_details)

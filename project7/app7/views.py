from django.shortcuts import render

# Create your views here.
def aadhar(request):
    aadhar_details={"adhar_input":
                    [
                    {"name":'bnk',"num":1234, "pin":[752013,752014,752016],},
                    {"name":'bubun',"num":1234567,"pin":[752013,752014,752016]},
                    {"name":'sipun',"num":1234567,"pin":[752013,752016]},
                    {"name":'bmk',"num":10002,"pin":[752013,752014]},
                    {"name":'m.kar',"num":10000,"pin":[752016]},
                    {"name":'b.kar',"num":200000},
                    ]}
    return render(request,"aadhar.html",aadhar_details)            

#new fun
def student(request):
    student_details={"student_input":
                        [{"stdname":"bnk","roll_num":23,"marks":[68,65,13,'A',10]},
                        {"stdname":"bubun","roll_num":98,"marks":[77,30,88,32,40]},
                        {"stdname":"sipun","roll_num":76,"marks":['A',23,44,50,26]},
                        {"stdname":"kar","roll_num":65,"marks":[66,32,98,88,22]},
                         ]   }
    return render(request,"student1.html",student_details)                     

#new fun2
def pancard(request):
    pancard_details={"pancard_input":
                        [{"pancardname":"bnk","pancard_num":"hyuj786","location":['boudh','kandhamal','nayagarh']},
                        {"pancardname":"bubun","pancard_num":"hgt568","location":['malakangiri','keonjhar','bargarh']},
                        {"pancardname":"sipun","pancard_num":"nhj6759","location":['sambalpur','sonepur','angul']},
                        {"pancardname":"kar","pancard_num":"mhju765","location":['khurdha','cuttack','puri']},
                         ]   }
    return render(request,"pancard.html",pancard_details)                  
#new fun3
def bank(request):
    bank_details={"bank_input":
                        [{"bankname":"sbi","acc_type":"saving","ifsc_code":"sbin0007654","location":['boudh','kandhamal','nayagarh'],"state":['OD','TS','WB','TN']},
                        {"bankname":"indian","acc_type":"current","ifsc_code":"idib000d039","location":['malakangiri','keonjhar','bargarh'],"state":['OD','TS','WB','TN']},
                        {"bankname":"axis","acc_type":"current","ifsc_code":"axis00789","location":['sambalpur','sonepur','angul'],"state":['OD','TS','WB','TN']},
                        {"bankname":"uco","acc_type":"current","ifsc_code":"uco098765","location":['khurdha','cuttack','puri'],"state":['OD','TS','WB','TN']},
                         ]   }
    return render(request,"bank.html",bank_details)         
    












    
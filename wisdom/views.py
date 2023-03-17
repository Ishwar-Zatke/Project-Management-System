from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from wiseapp import models, forms

from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
 

def  index(request):
    return render(request,'index.html')


def login(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        if (username=="admin") and (password=="admin"):
            return render(request,'middle.html')
        else:
            return HttpResponse("Login Failed")


def Viewdata(request):
    obj2=models.DataStudent.objects.all
    return render(request,'viewdata.html',{'data':obj2})


def updatedata(request,id):
    
    obj5=models.DataStudent.objects.get(id=id)
    obj6=forms.todoAddForm(instance=obj5)
    if request.method=='POST':
        todoAdd=forms.todoAddForm(request.POST,instance=obj5)
        if todoAdd.is_valid():
            todoAdd.save()
            print("Data saved")
            return redirect('/viewdata/')
    return render(request,'updatedata.html',{
        'form':obj6,
        'obj5':obj5
    })    
    
    
def deldata(request,id):
    
        obj3=models.DataStudent.objects.get(id=id)
        obj3.delete()
        obj4=models.DataStudent.objects.all

        return render(request,'viewdata.html',{'data':obj4})


def SearchEmployee(request):
    # Define model
    if 'q' in request.GET:
        q=request.GET['q']
        queryset = models.DataStudent.objects.filter(student_name =q)
    if 'r' in request.GET:
        r=request.GET['r']
        queryset = models.DataStudent.objects.filter(student_project_type =r)
    
    return render(request,'searchdata.html',{'data': queryset})


def AddStudent(request):
    return render(request,'studentdata.html')


def studentdata(request):
    Name=request.POST.get("name")
    Address=request.POST.get("address")
    Email=request.POST.get("email")
    Mobile=request.POST.get("mobile")
    Project_Type=request.POST.get("projecttype")   #UG/PG/PhD/Industrial
    Project_Name=request.POST.get("projectname")
    Project_Code=request.POST.get("projectcode")
    Total_Fees=request.POST.get("totalfees")
    ModeOfPayment=request.POST.get("ModeOfPayment")
    DateofPayment=request.POST.get("DateofPayment")
    addObj = models.DataStudent(student_name=Name, student_address=Address, student_email = Email, student_mobile = Mobile, student_project_type = Project_Type, student_project_name = Project_Name, student_project_code = Project_Code, student_project_fees = Total_Fees, student_project_payment_mode = ModeOfPayment, student_date_of_payment=DateofPayment)
    addObj.save()
    dict1={'Name':Name,'Address':Address,'Email':Email,'Mobile':Mobile,'Project_Type':Project_Type,'Project_Name':Project_Name,'Project_Code':Project_Code,'Total_Fees':Total_Fees,'ModeOfPayment':ModeOfPayment,'DateofPayment':DateofPayment}    
    
    return render(request,'showdata.html',dict1)
    
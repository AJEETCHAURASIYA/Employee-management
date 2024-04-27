from django.shortcuts import render ,redirect
from . models import Employee

# Create your views here.
def index(request):
    emp=Employee.objects.all() # select * from Employee
    return render(request,'index.html',{'emp':emp})
def registration(request):
    if request.method=="POST":
        empid=request.POST['empid']
        empname=request.POST['empname']
        department=request.POST['department']
        salary=request.POST['salary']
        emp=Employee(empid=empid,empname=empname,department=department,salary=salary)
        # emp.empid=empid
        # emp.empname=empname
        # emp.department=department
        # emp.salary=salary
        emp.save()
        return redirect('index')
    return render(request,'registration.html')
def delemp(request,id):
    emp=Employee.objects.get(empid=id)
    emp.delete()
    return redirect('index')
def showemp(request,id):
    emp=Employee.objects.get(empid=id)
    return render(request,'showemp.html',{'emp':emp})
def updateemp(request):
    empid=request.POST['empid']
    empname=request.POST['empname']
    department=request.POST['department']
    salary=request.POST['salary']
    Employee.objects.filter(empid=empid).update(empname=empname,department=department,salary=salary)
    return redirect('index')

    
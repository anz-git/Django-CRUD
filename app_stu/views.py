from django.shortcuts import render,redirect
from app_stu.models import Student
from app_stu.forms import StudentForm
# Create your views here.

def create(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass 
    else:
        form = StudentForm()
    return render(request,'create.html',{'form':form})   

def show(request):
    std = Student.objects.all()
    return render(request,'show.html',{'student':std})

def edit(request,id):
    std = Student.objects.get(id=id)
    return render(request,'edit.html',{'student':std}) 

def update(request,id):
    std = Student.objects.get(id=id)
    form = StudentForm(request.POST,instance = std)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'student':std})

def dlt(request,id):
    std = Student.objects.get(id=id)
    std.delete()
    return redirect('/show')


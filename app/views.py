from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def home(request):
    studentobj=student.objects.all()
    
    return render(request,'index.html',{'data':studentobj})

def update(request):
    data={}
    if request.method=='POST':
        roll=request.POST.get('roll')
        print(roll)
        studentobj=student.objects.get(roll=roll)
        data={'obj':studentobj}
        
        
    return render(request,'modify.html',data)

def update1(request):
    if request.method=='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        fac=request.POST.get('faculty')
        ph=request.POST.get('phone')
        obj=student.objects.get(id=id)
        obj.name=name
        obj.faculty=fac
        obj.phone=ph
        obj.save()
        messages.success(request,"Data Updated successfully")
        return redirect('home')
        
        
    


    
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        fac=request.POST.get('fac')
        ph=request.POST.get('phone')
        roll=request.POST.get('roll')
        
        en=student(name=name,faculty=fac,roll=roll,phone=ph)
        en.save()
        messages.success(request,"Data Added successfully")
        return redirect('home')
        
        
        
    
    return render(request,'add.html')

def delete(request):
    if request.method=='POST':
        id=request.POST.get('id')
        obj=student.objects.get(roll=id)
        obj.delete()
        messages.warning(request,"Data deleted successfully") 
        return redirect('home')
    return render(request,'delete.html')

def delete1(request,id):
    obj=student.objects.get(id=id)
    obj.delete()
    messages.success(request,"Data deleted successfully")
    return redirect('home')
    

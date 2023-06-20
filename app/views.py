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
    return render(request,'modify.html')

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
    

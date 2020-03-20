from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from . import forms
from hr_app.forms import EmployeeForm
from hr_app.models import EmployeeDetails

# Create your views here.
def EmployeeView(request):
    form=forms.EmployeeForm()
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('display/')
        else:
            pass
    return render(request,'employee.html',{'form':form})


def display(request):
    employees = EmployeeDetails.objects.all()  
    return render(request,"display.html",{'employees':employees})

def TemplateView(request):
    form=forms.EmployeeForm()
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    return render(request,'template.html',{'form':form})

def DocumentView(request):
    form=forms.DocumentsForm()
    if request.method=='POST':
        form=forms.DocumentsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('files uploaded Successfully')
        else:
            return HttpResponse('files upload failed!!! try again')
    return render(request,'documents.html',{'form':form})

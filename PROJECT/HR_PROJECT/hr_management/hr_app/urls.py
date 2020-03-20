from django.contrib import admin
from django.urls import path
from hr_app import views

urlpatterns = [
    
    path('employee/',views.EmployeeView),
    path('display/',views.display),
    path('template/',views.TemplateView),
    path('documents/',views.DocumentView),
    

]
from django.shortcuts import render
from . import models
from .models import Doctors
from .forms import BookingForm

def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def contacts(request):
    return render(request,'contacts.html')

def departments(request):
    dict_dpt={
        'dept':models.Departments.objects.all()
    }
    return render(request,'departments.html',dict_dpt)

def doctors(request):
    dict_doc={
        'doctors':models.Doctors.objects.all()

    }
    
    return render(request,'doctors.html',dict_doc)


def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
            


    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

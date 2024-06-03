from django.http import HttpResponse
from django.shortcuts import render
from .models import Department,Doctors
from .forms import BookingForm
# Create your views here.
def homepage(request):
    return render(request,'HomePage.html')
def aboutpage(request):
    return render(request, 'AboutPage.html')
def bookingpage(request):
    if request.method == 'POST':
        bookingform=BookingForm(request.POST)
        if bookingform.is_valid():
            bookingform.save()
            return render(request,'confirmation.html')
    bookingform=BookingForm()
    dict_form={
        'form':bookingform
    }
    return render(request, 'BookingPage.html',dict_form)
def doctorspage(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'DoctorsPage.html', dict_docs)

def contactpage(request):
    return render(request, 'ContactPage.html')
def departmentpage(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request, 'DepartmentPage.html',dict_dept)

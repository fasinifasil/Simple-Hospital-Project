from django.urls import path

from App1 import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('aboutpage',views.aboutpage,name='aboutpage'),
    path('bookingpage',views.bookingpage,name='bookingpage'),
    path('doctorspage',views.doctorspage,name='doctorspage'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('departmentpage',views.departmentpage,name='departmentpage'),
]
from django.contrib import admin
from .models import Department,Doctors,Booking
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
  list_display = ("Patient_name", "Doctor_name", "Booking_date","Booked_on")
admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Booking,BookingAdmin)


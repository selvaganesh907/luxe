from django.contrib import admin
from .models import Service, Professional, Booking
from .models import Contact

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('is_active',)
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'customer_name', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('customer_name', 'customer_phone', 'customer_email')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
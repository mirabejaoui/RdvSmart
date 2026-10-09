from django.contrib import admin

from .models import Appointment, Patient, Practitioner


@admin.register(Practitioner)
class PractitionerAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "specialty", "phone"]
    search_fields = ["last_name", "first_name"]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "birth_date", "gender", "phone"]
    search_fields = ["last_name", "first_name", "phone"]
    list_filter = ["gender"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["start_at", "patient", "practitioner", "status", "sms_reminder_sent"]
    list_filter = ["status", "practitioner"]
    search_fields = ["patient__last_name", "patient__first_name"]
    date_hierarchy = "start_at"

from django.contrib import admin

from hospitalapp import models

# Register your models here.

admin.site.register(models.Login)
admin.site.register(models.doctor)
admin.site.register(models.patient)
admin.site.register(models.department)
admin.site.register(models.DocSchedule)
admin.site.register(models.Appointment)
admin.site.register(models.DoctorNotification)
admin.site.register(models.PatientNotification)
admin.site.register(models.PatientData)
admin.site.register(models.Feedback)


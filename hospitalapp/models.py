from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept_name


class doctor(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='Doctor')
    name = models.CharField(max_length=100)
    department = models.ForeignKey(department, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    Image = models.ImageField(upload_to='images/')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class patient(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12,unique=True, validators=[MinLengthValidator(12)])
    email = models.EmailField()

    def __str__(self):
        return self.name


class DocSchedule(models.Model):
    Doc_name = models.ForeignKey(doctor, on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Start_time = models.TimeField()
    End_time = models.TimeField()

    def __str__(self):
        return self.Doc_name


class Appointment(models.Model):
    user = models.ForeignKey(patient, on_delete=models.CASCADE, related_name='appointment')
    Schedule = models.ForeignKey(DocSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __int__(self):
        return self.status


class DoctorNotification(models.Model):
    date = models.DateField(auto_now=True)
    subject = models.CharField(max_length=200)


class PatientNotification(models.Model):
    date = models.DateField(auto_now=True)
    subject = models.CharField(max_length=200)




class PatientData(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Doctor_name = models.ForeignKey(doctor, on_delete=models.DO_NOTHING)
    Title = models.CharField(max_length=100)
    Patient_data = models.FileField(upload_to='data/')


class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user



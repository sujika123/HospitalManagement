from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from hospitalapp.forms import loginform, doctorlogin, patientlogin
from hospitalapp.models import doctor


# Create your views here.


def index(request):
    data = doctor.objects.filter(status=True)
    return render(request, 'index.html',{'data':data})

def dash(request):
    return render(request, "admin/dash.html")

def loginview(request):
    return render(request, "sign-in.html")

def register(request):
    return render(request, "sign-up.html")


def doctor_registration(request):
    form1 = loginform()
    form2 = doctorlogin()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = doctorlogin(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_doctor = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()

            return redirect('login_view')

    return render(request, 'doctor/doctor_registration.html', {'form1': form1, 'form2': form2})


def patient_registration(request):
    form1 = loginform()
    form2 = patientlogin()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = patientlogin(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_patient = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('login_view')

    return render(request, 'patient/patient_registration.html', {'form1': form1, 'form2': form2})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            if user.is_staff:
                login(request, user)
                return redirect('admindashboard')

            elif user.is_patient:
                login(request, user)
                return redirect('patientdashboard')

            elif user.is_doctor and user.Doctor.status == 1:
                print(user)
                login(request, user)
                return redirect('doctordashboard')
            else:
                messages.info(request, 'You are not a verified user')

        else:
            messages.info(request, 'invalid Credentials')
    return render(request, 'sign-in.html')


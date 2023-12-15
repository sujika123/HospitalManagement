from django.contrib import messages
from django.shortcuts import render, redirect

from hospitalapp.forms import PatientDataForm, FeedbackForm
from hospitalapp.models import department, doctor, DocSchedule, patient, Appointment, PatientNotification, Feedback


def patientdashboard(request):
    return render(request, 'patient/dash.html')


def patient_view_department(request):
    data = department.objects.all()
    return render(request, 'patient/viewDepartments.html', {'data': data})


def patient_view_doctor(request):
    data = doctor.objects.filter(status=True)
    return render(request, 'patient/viewDoctors.html', {'data': data})


def patient_view_schedule(request):
    data = DocSchedule.objects.all()
    return render(request, 'patient/viewSchedule.html', {'data': data})


def book_apppointment(request, id):
    data = DocSchedule.objects.get(id=id)
    p = patient.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=p, Schedule=data)
    if appointment.exists():
        messages.info(request, 'You have already requested for this slot')
        return redirect('patient_view_schedule')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = p
            obj.Schedule = data
            obj.save()
            messages.info(request, 'Appointment successful..!!')
            return redirect('view_appointment')
    return render(request, 'patient/BookAppointment.html', {'data': data})


def view_appointment(request):
    p = patient.objects.get(user=request.user)
    data = Appointment.objects.filter(user=p)
    return render(request, 'patient/viewAppointment.html', {'data': data})


# patient Data

def patient_data(request):
    form = PatientDataForm()
    u = request.user
    if request.method == 'POST':
        form = PatientDataForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'The data sent Successfully..!!')
            return redirect('patient_data')
    return render(request, 'patient/patient_data.html', {'form': form})


# Notification

def patient_view_notification(request):
    data = PatientNotification.objects.all()
    return render(request, 'patient/viewNotification.html', {'data': data})


# Feedback

def AddFeedback(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect('view_feedback')
    return render(request, 'patient/AddFeedback.html', {'form': form})

def view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'patient/viewFeedback.html', {'data': data})


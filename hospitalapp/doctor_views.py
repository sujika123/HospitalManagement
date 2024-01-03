from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hospitalapp.models import department, patient, doctor, Appointment, PatientData, DoctorNotification, Feedback


@login_required(login_url='login_view')
def doctordashboard(request):
    return render(request, 'doctor/dash.html')


# Department

@login_required(login_url='login_view')
def doc_view_department(request):
    data=department.objects.all()
    return render(request,'doctor/viewDepartments.html',{'data':data})


# Patient

@login_required(login_url='login_view')
def doc_view_patients(request):
    data = patient.objects.all()
    return render(request, 'doctor/viewPatients.html', {'data': data})


# Appointment

@login_required(login_url='login_view')
def doc_view_appointments(request):
    doc = doctor.objects.get(user=request.user)
    data = Appointment.objects.filter(Schedule__Doc_name=doc)
    return render(request, 'doctor/viewAppointments.html', {'data': data})


# Patient Data

@login_required(login_url='login_view')
def view_patient_data(request):
    doc = doctor.objects.get(user=request.user)
    data = PatientData.objects.filter(Doctor_name=doc)
    return render(request, 'doctor/view_patient_data.html', {'data': data})

@login_required(login_url='login_view')
def delete_patient_data(request, id):
    data = PatientData.objects.get(id=id)
    data.delete()
    return redirect('view_patient_data')


# Notification

@login_required(login_url='login_view')
def doc_view_notificaction(request):
    data = DoctorNotification.objects.all()
    return render(request, 'doctor/viewNotification.html', {'data': data})


# Feedbacks

@login_required(login_url='login_view')
def doc_view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'doctor/viewFeedback.html', {'data': data})


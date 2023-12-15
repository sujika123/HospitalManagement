from django.shortcuts import render, redirect

from hospitalapp.models import department, patient, doctor, Appointment, PatientData, DoctorNotification, Feedback


def doctordashboard(request):
    return render(request, 'doctor/dash.html')


def doc_view_department(request):
    data=department.objects.all()
    return render(request,'doctor/viewDepartments.html',{'data':data})

def doc_view_patients(request):
    data = patient.objects.all()
    return render(request, 'doctor/viewPatients.html', {'data': data})

def doc_view_appointments(request):
    doc = doctor.objects.get(user=request.user)
    data = Appointment.objects.filter(Schedule__Doc_name=doc)
    return render(request, 'doctor/viewAppointments.html', {'data': data})

# Patient Data

def view_patient_data(request):
    doc = doctor.objects.get(user=request.user)
    data = PatientData.objects.filter(Doctor_name=doc)
    return render(request, 'doctor/view_patient_data.html', {'data': data})

def delete_patient_data(request, id):
    data = PatientData.objects.get(id=id)
    data.delete()
    return redirect('view_patient_data')


# Notification

def doc_view_notificaction(request):
    data = DoctorNotification.objects.all()
    return render(request, 'doctor/viewNotification.html', {'data': data})

# Feedbacks

def doc_view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'doctor/viewFeedback.html', {'data': data})


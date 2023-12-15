from django.contrib import messages
from django.shortcuts import redirect, render

from hospitalapp.forms import departmentform, doctorlogin, patientlogin, ScheduleForm, DoctorNotificationForm, \
    PatientNotificationForm
from hospitalapp.models import department, doctor, patient, DocSchedule, Appointment, DoctorNotification, \
    PatientNotification, Feedback


def admindashboard(request):
    return render(request, 'admin/dash.html')


def add_department(request):
    form = departmentform()
    if request.method == 'POST':
        form = departmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_department')
    return render(request, 'admin/adddepartments.html', {'form': form})



def view_department(request):
    data = department.objects.all()
    return render(request, 'admin/viewdepartments.html', {'data': data})

def updatedep(request, id):
    data = department.objects.get(id=id)
    form = departmentform(instance=data)
    if request.method == 'POST':
        form = departmentform(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_department')
    return render(request, 'admin/updatedepartment.html', {'form': form})



def deletedep(request, id):
    data = department.objects.get(id=id)
    data.delete()
    return redirect('view_department')


def doctor_view(request):
    data = doctor.objects.filter(status=True)
    return render(request, 'admin/viewdoctors.html', {'data': data})



def doctor_delete(request, pk):
    data = doctor.objects.get(pk=pk)
    data.delete()

    return redirect('doctor_view')



def updatedoctor(request, pk):
    data = doctor.objects.get(pk=pk)
    form = doctorlogin(instance=data)
    if request.method == 'POST':
        form = doctorlogin(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('doctor_view')
    return render(request, 'admin/updatedoctor.html', {'form': form})



def doctor_approval_list(request):
    data = doctor.objects.all()
    return render(request, 'admin/doctor_approval.html', {'data': data})



def approve_doctor(request, user_id):
    data = doctor.objects.get(user_id=user_id)
    data.status = 1
    data.save()
    messages.info(request, 'Doctor is approved to log in')
    return redirect('doctor_approval_list')



def reject_doctor(request, user_id):
    data = doctor.objects.get(user_id=user_id)
    data.status = 2
    data.save()
    messages.info(request, 'Doctor approval request  is rejected')
    return redirect('doctor_approval_list')

def view_patient(request):
    data = patient.objects.all()
    return render(request, 'admin/view_patient.html', {'data': data})

def updatepatient(request, id):
    data = patient.objects.get(id=id)
    form = patientlogin(instance=data)
    if request.method == 'POST':
        form = patientlogin(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_patient')
    return render(request, 'admin/updatepatient.html', {'form': form})


def delete_patient(request, id):
    data = patient.objects.get(id=id)
    data.delete()
    return redirect('view_patient')

# Schedule

def add_schedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_schedule')
    return render(request, 'admin/addSchedule.html', {'form': form})



def view_schedule(request):
    data = DocSchedule.objects.all()
    return render(request, 'admin/viewSchedule.html', {'data': data})



def delete_schedule(request, id):
    data = DocSchedule.objects.get(id=id)
    data.delete()
    return redirect('view_schedule')

# Appointment
def booking_view(request):
    data = Appointment.objects.all()
    return render(request, 'admin/viewBooking.html', {'data': data})

def approve_appo(request, id):
    data = Appointment.objects.get(id=id)
    data.status = 1
    data.save()
    messages.info(request, 'Appointment Confirmed')
    return redirect('booking_view')

def reject_appo(request, id):
    data = Appointment.objects.get(id=id)
    data.status = 2
    data.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('booking_view')


# Notification

def add_doc_notification(request):
    form = DoctorNotificationForm()
    if request.method == 'POST':
        form = DoctorNotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_doc_notifications')
    return render(request, 'admin/add_Docnotification.html', {'form': form})



def add_pat_notification(request):
    form = PatientNotificationForm()
    if request.method == 'POST':
        form = PatientNotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pat_notifications')
    return render(request, 'admin/add_PatNotification.html', {'form': form})



def view_doc_notifications(request):
    data = DoctorNotification.objects.all()
    return render(request, 'admin/viewDoctorNotification.html', {'data': data})



def view_pat_notifications(request):
    data = PatientNotification.objects.all()
    return render(request, 'admin/viewPatientNotification.html', {'data': data})



def delete_docnotification(request, id):
    data = DoctorNotification.objects.get(id=id)
    data.delete()
    return redirect('view_doc_notifications')



def delete_patnotification(request, id):
    data = PatientNotification.objects.get(id=id)
    data.delete()
    return redirect('view_pat_notifications')


# Feedback

def admin_view_feedbacks(request):
    data = Feedback.objects.all()
    return render(request, 'admin/viewfeedback.html', {'data': data})


def delete_feedbacks(request, id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('admin_view_feedbacks')


def reply_feedback(request, id):
    data = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        data.reply = r
        data.save()
        return redirect('admin_view_feedbacks')
    return render(request, 'admin/replyFeedback.html', {'data': data})


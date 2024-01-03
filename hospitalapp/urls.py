from django.urls import path

from hospitalapp import views, admin_views, patient_views, doctor_views

urlpatterns = [

    path('',views.index,name="index"),
    path('doctor_registration', views.doctor_registration, name='doctor_registration'),
    path('patient_registration', views.patient_registration, name='patient_registration'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),


# ADMIN URLS

    path('admindashboard', admin_views.admindashboard, name='admindashboard'),
    path('add_department', admin_views.add_department, name='add_department'),
    path('view_department', admin_views.view_department, name='view_department'),
    path('updatedep/<int:id>/', admin_views.updatedep, name='updatedep'),
    path('deletedep/<int:id>/', admin_views.deletedep, name='deletedep'),
    path('doctor_view', admin_views.doctor_view, name='doctor_view'),
    path('updatedoctor/<int:pk>/', admin_views.updatedoctor, name='updatedoctor'),
    path('doctor_delete/<int:pk>/', admin_views.doctor_delete, name='doctor_delete'),
    path('doctor_approval_list', admin_views.doctor_approval_list, name='doctor_approval_list'),
    path('approve_doctor/<int:user_id>/', admin_views.approve_doctor, name='approve_doctor'),
    path('reject_doctor/<int:user_id>/', admin_views.reject_doctor, name='reject_doctor'),
    path('view_patient', admin_views.view_patient, name='view_patient'),
    path('updatepatient/<int:id>/', admin_views.updatepatient, name='updatepatient'),
    path('delete_patient/<int:id>/', admin_views.delete_patient, name='delete_patient'),
    path('add_schedule', admin_views.add_schedule, name='add_schedule'),
    path('view_schedule', admin_views.view_schedule, name='view_schedule'),
    path('delete_schedule/<int:id>/', admin_views.delete_schedule, name='delete_schedule'),
    path('booking_view', admin_views.booking_view, name='booking_view'),
    path('approve_appo/<int:id>/', admin_views.approve_appo, name='approve_appo'),
    path('reject_appo/<int:id>/', admin_views.reject_appo, name='reject_appo'),
    path('add_doc_notification', admin_views.add_doc_notification, name='add_doc_notification'),
    path('view_doc_notifications', admin_views.view_doc_notifications, name='view_doc_notifications'),
    path('delete_docnotification/<int:id>/', admin_views.delete_docnotification, name='delete_docnotification'),
    path('add_pat_notification', admin_views.add_pat_notification, name='add_pat_notification'),
    path('view_pat_notifications', admin_views.view_pat_notifications, name='view_pat_notifications'),
    path('delete_patnotification/<int:id>/', admin_views.delete_patnotification, name='delete_patnotification'),
    path('admin_view_feedbacks', admin_views.admin_view_feedbacks, name='admin_view_feedbacks'),
    path('delete_feedbacks/<int:id>/', admin_views.delete_feedbacks, name='delete_feedbacks'),
    path('reply_feedback/<int:id>/', admin_views.reply_feedback, name='reply_feedback'),





# DOCTOR URLS
    path('doctordashboard', doctor_views.doctordashboard, name='doctordashboard'),
    path('doc_view_department', doctor_views.doc_view_department, name='doc_view_department'),
    path('doc_view_patients', doctor_views.doc_view_patients, name='doc_view_patients'),
    path('doc_view_appointments', doctor_views.doc_view_appointments, name='doc_view_appointments'),
    path('view_patient_data', doctor_views.view_patient_data, name='view_patient_data'),
    path('delete_patient_data/<int:id>/', doctor_views.delete_patient_data, name='delete_patient_data'),
    path('doc_view_notificaction', doctor_views.doc_view_notificaction, name='doc_view_notificaction'),
    path('doc_view_feedback', doctor_views.doc_view_feedback, name='doc_view_feedback'),




# PATIENT URLS
    path('patientdashboard', patient_views.patientdashboard, name='patientdashboard'),
    path('patient_view_department', patient_views.patient_view_department, name='patient_view_department'),
    path('patient_view_doctor', patient_views.patient_view_doctor, name='patient_view_doctor'),
    path('patient_view_schedule', patient_views.patient_view_schedule, name='patient_view_schedule'),
    path('book_apppointment/<int:id>/', patient_views.book_apppointment, name='book_apppointment'),
    path('view_appointment', patient_views.view_appointment, name='view_appointment'),
    path('patient_data', patient_views.patient_data, name='patient_data'),
    path('patient_view_notification', patient_views.patient_view_notification, name='patient_view_notification'),
    path('AddFeedback', patient_views.AddFeedback, name='AddFeedback'),
    path('view_feedback', patient_views.view_feedback, name='view_feedback'),


]

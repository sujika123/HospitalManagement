import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from hospitalapp.models import Login, doctor, patient, department, DocSchedule, DoctorNotification, PatientNotification, \
    PatientData, Feedback


class loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class doctorlogin(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'
        exclude = ('user', 'status',)


class patientlogin(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'
        exclude = ('user',)


class departmentform(forms.ModelForm):
    class Meta:
        model = department
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleForm(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    Start_time = forms.TimeField(widget=TimeInput)
    End_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = DocSchedule
        fields = ('Doc_name', 'Date', 'Start_time', 'End_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("Start_time")
        end = cleaned_data.get("End_time")
        date = cleaned_data.get("Date")
        if start > end:
            raise forms.ValidationError("End Time should be greater than start Time.")

        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data


class DoctorNotificationForm(forms.ModelForm):
    class Meta:
        model = DoctorNotification
        fields = '__all__'


class PatientNotificationForm(forms.ModelForm):
    class Meta:
        model = PatientNotification
        fields = '__all__'


class PatientDataForm(forms.ModelForm):
    class Meta:
        model = PatientData
        fields = ('Title','Doctor_name','Patient_data',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ('reply', 'user',)


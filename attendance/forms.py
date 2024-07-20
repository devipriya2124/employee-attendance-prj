from django import forms
from .models import Attendance, LeaveRequest


class AttendanceForm(forms.ModelForm):   
  class Meta:   
        model = Attendance  
        exclude=['date']
        fields = [ 'user','date','status', 'check_in_time','check_out_time']  

class LeaveRequestForm(forms.Form):
    # Define your form fields here
    start_date = forms.DateField()
    end_date = forms.DateField()
    leave_reason = forms.CharField(max_length=255)
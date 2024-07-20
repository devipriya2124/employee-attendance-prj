from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance, LeaveRequest
from .forms import AttendanceForm, LeaveRequestForm  
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  


def index(request):
    # Your view logic here
    return render(request, 'attendance/index.html')
 
@login_required
def user_dashboard(request):
    user = request.user
    attendance_records = Attendance.objects.filter(user=user)
    leave_requests = LeaveRequest.objects.filter(user=user)
    context = {
        'attendance_records': attendance_records,
        'leave_requests': leave_requests
    }
    return render(request, 'attendance/user_dashboard.html', context)

@login_required
def mark_attendance(request):
    user = request.user
    if request.method == 'POST': 
        form = AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form without the 'date' field
            instance = form.save(commit=False)
            # Perform additional logic if needed
            instance.save()
            return redirect('index')  # Replace with appropriate redirect
    else:
        form = AttendanceForm() 
    return render(request, 'attendance/mark_attendance.html',{'form':form})  

@login_required
def mark_check_in(request):
    user = request.user
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form without the 'date' field
            instance = form.save(commit=False)
            instance.user = request.user  # Assign the current user to the attendance
            instance.save()
            return redirect('user_dashboard')  # Redirect to the user dashboard after saving
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})
@login_required
def request_leave(request):
    user = request.user
    if request.method == 'POST':
        leave_request = LeaveRequest.objects.create(
            user=user,
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'], 
             reason=request.POST['reason'] 
        )
        leave_request.save()
        return redirect('user_dashboard')
    return render(request, 'attendance/request_leave.html')

@login_required
def admin_dashboard(request):
    users = User.objects.all()
    leave_requests = LeaveRequest.objects.all() 
    # print(leave_requests)
    context = {
        'users': users,
        'leave_requests': leave_requests
    }
    return render(request, 'attendance/admin_dashboard.html', context) 

@login_required
def approve_leave(request, leave_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    leave_request.status = 'Approved'
    leave_request.save()
    return redirect('admin_dashboard') 
   

@login_required
def reject_leave(request, leave_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    leave_request.status = 'Rejected'
    leave_request.save()
    return redirect('admin_dashboard')  

@login_required
def attendance_view(request): 
    if request.user.is_authenticated: 
        attendances = Attendance.objects.filter(user=request.user)
        return render(request, 'attendance/attendance_view.html', {'attendances': attendances})    
    else: 
        return redirect('login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_attendance')
        else:
            return render(request, 'attendance/admin_login.html', {'error': 'Invalid credentials or not an admin'})
    return render(request,'attendance/admin_login.html')

@login_required
def admin_attendance(request):
    if request.user.is_staff:
        attendances = Attendance.objects.all()
        return render(request, 'attendance/attendance_view.html', {'attendances': attendances})
    else:
        return redirect('admin_login')  # Redirect to admin login if not an admin









 





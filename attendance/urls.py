from django.urls import path 
from .views import admin_login, admin_attendance
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),  
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('request_leave/', views.request_leave, name='request_leave'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),   
    path('attendace/', views.attendance_view, name='attendance_view'),  
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_attendance/', admin_attendance, name='admin_attendance'), 

]

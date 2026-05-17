from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # QR check-in (public — scanned from QR code)
    path('checkin/<uuid:token>/', views.qr_checkin_view, name='qr_checkin'),
    # Manual fallback check-in (no QR needed — applicant types their User ID)
    path('checkin/', views.manual_checkin_view, name='manual_checkin'),

    # Applicant portal
    path('dashboard/', views.applicant_dashboard_view, name='applicant_dashboard'),

    # Admin
    path('admin-panel/', views.admin_dashboard_view, name='admin_dashboard'),
    path('admin-panel/session/<int:session_id>/', views.session_detail_view, name='session_detail'),
    path('admin-panel/session/<int:session_id>/mark-absent/', views.mark_absent_view, name='mark_absent'),
    path('admin-panel/session/<int:session_id>/mark/<int:applicant_id>/', views.admin_mark_attendance_view, name='admin_mark_attendance'),
    path('admin-panel/session/<int:session_id>/export/csv/', views.export_csv_view, name='export_csv'),
    path('admin-panel/session/<int:session_id>/export/excel/', views.export_excel_view, name='export_excel'),
]

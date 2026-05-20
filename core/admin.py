from django.contrib import admin
from .models import Applicant, Session, AttendanceRecord


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user__email', 'cohort', 'phone', 'created_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'cohort')
    list_filter = ('cohort',)

    def user__email(self, obj):
        return obj.user.email
    user__email.short_description = 'Email'


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'start_time', 'end_time', 'late_after', 'checkin_code', 'is_active', 'qr_token')
    list_filter = ('is_active',)
    search_fields = ('title',)
    readonly_fields = ('qr_token', 'checkin_code')


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'session', 'status', 'checked_in_at')
    list_filter = ('status', 'session')
    search_fields = ('applicant__user__username', 'applicant__user__first_name')

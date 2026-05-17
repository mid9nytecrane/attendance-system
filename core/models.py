from django.db import models
from django.contrib.auth.models import User
import uuid


class Applicant(models.Model):
    COHORT_CHOICES = [
        ('cohort 1', 'Cohort 1'),
        ('cohort 2', 'Cohort 2'),
        ('cohort 3', 'Cohort 3'),
        ('cohort 4', 'Cohort 4')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='applicant')
    phone = models.CharField(max_length=10, blank=True)
    cohort = models.CharField(max_length=50, choices=COHORT_CHOICES, blank=True, help_text="e.g. Cohort 1, Batch A")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"

    def attendance_summary(self):
        records = self.attendance_records.all()
        return {
            'total': records.count(),
            'present': records.filter(status='present').count(),
            'late': records.filter(status='late').count(),
            'absent': records.filter(status='absent').count(),
        }


class Session(models.Model):
    date = models.DateField(unique=True)
    title = models.CharField(max_length=200, blank=True, help_text="e.g. Week 3 - Python Basics")
    start_time = models.TimeField()
    late_after = models.TimeField(help_text="Check-ins after this time are marked late")
    qr_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_active = models.BooleanField(default=False, help_text="Only one session should be active at a time")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Session {self.date} — {self.title or 'No title'}"

    def attendance_stats(self):
        records = self.attendance_records.all()
        total_applicants = Applicant.objects.count()
        checked_in = records.count()
        return {
            'total_applicants': total_applicants,
            'present': records.filter(status='present').count(),
            'late': records.filter(status='late').count(),
            'absent': total_applicants - checked_in,
        }


class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ]

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='attendance_records')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
    checked_in_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('applicant', 'session')
        ordering = ['-session__date']

    def __str__(self):
        return f"{self.applicant} — {self.session.date} — {self.status}"

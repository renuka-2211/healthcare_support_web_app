from django.db import models

class SupportRequest(models.Model):
    ISSUE_CHOICES = [
        ('medical', 'Medical Help'),
        ('insurance', 'Insurance Query'),
        ('appointment', 'Doctor Appointment'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    issue_type = models.CharField(max_length=50, choices=ISSUE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

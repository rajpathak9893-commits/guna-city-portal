from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    JOB_TYPES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Remote', 'Remote'),
        ('Contract', 'Contract'),
    )

    title        = models.CharField(max_length=200)
    company      = models.CharField(max_length=200)
    location     = models.CharField(max_length=200)
    salary       = models.CharField(max_length=100)
    description  = models.TextField()
    job_type     = models.CharField(max_length=50, choices=JOB_TYPES)
    experience   = models.CharField(max_length=100, blank=True)
    deadline     = models.DateField(null=True, blank=True)
    phone        = models.CharField(max_length=15, blank=True)
    whatsapp     = models.CharField(max_length=15, blank=True)
    address      = models.TextField(blank=True)
    company_logo = models.ImageField(upload_to='job_logos/', blank=True, null=True)
    is_approved  = models.BooleanField(default=True)  # default True rakho
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
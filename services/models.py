from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):

    CATEGORY_CHOICES = (
        # Local
        ('Plumber',       'Plumber'),
        ('Electrician',   'Electrician'),
        ('Carpenter',     'Carpenter'),
        ('Painter',       'Painter'),
        ('Mechanic',      'Mechanic'),
        ('Cleaner',       'Cleaner'),
        ('Driver',        'Driver'),
        ('Security',      'Security Guard'),
        # Professional
        ('Tutor',         'Tutor / Teacher'),
        ('Doctor',        'Doctor'),
        ('Lawyer',        'Lawyer'),
        ('CA',            'CA / Accountant'),
        ('Designer',      'Graphic Designer'),
        ('Developer',     'Web / App Developer'),
        ('Photographer',  'Photographer'),
        ('Other',         'Other'),
    )

    AVAILABILITY_CHOICES = (
        ('Full-time',   'Full-time'),
        ('Part-time',   'Part-time'),
        ('Weekends',    'Weekends Only'),
        ('On-call',     'On Call'),
        ('By Appointment', 'By Appointment'),
    )

    user         = models.ForeignKey(User, on_delete=models.CASCADE)

    # Basic
    name         = models.CharField(max_length=200)
    category     = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    location     = models.CharField(max_length=200)
    price        = models.CharField(max_length=100)          # e.g. "₹500/visit"

    # Detailed
    description  = models.TextField(blank=True)
    experience   = models.CharField(max_length=100, blank=True)  # e.g. "5+ Years"
    timing       = models.CharField(max_length=200, blank=True)  # e.g. "9am - 6pm"
    availability = models.CharField(max_length=100, choices=AVAILABILITY_CHOICES, blank=True)
    phone        = models.CharField(max_length=15, blank=True)
    whatsapp     = models.CharField(max_length=15, blank=True)
    website      = models.URLField(blank=True)
    photo        = models.ImageField(upload_to='service_photos/', blank=True, null=True)

    # Full
    rating       = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    is_approved  = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
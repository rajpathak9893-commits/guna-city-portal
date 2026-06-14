from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    school_type = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='schools/', blank=True, null=True)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=200)
    courses = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='colleges/', blank=True, null=True)

    def __str__(self):
        return self.name


class Coaching(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    description = models.TextField()
    image = models.ImageField(upload_to='coaching/', blank=True, null=True)

    def __str__(self):
        return self.name
# from django.db import models


class Education(models.Model):

    CATEGORY_CHOICES = (
        ('School', 'School'),
        ('College', 'College'),
        ('Coaching', 'Coaching'),
        ('Course', 'Course'),
        ('Institute', 'Institute'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    description = models.TextField()

    location = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    website = models.URLField(blank=True)

    image = models.ImageField(
        upload_to='education/',
        blank=True,
        null=True
    )

    featured = models.BooleanField(default=False)

    admission_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# businesses/models.py

from django.db import models
from django.utils.text import slugify
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome class, e.g. fa-store")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Listing(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending Review'),
        ('inactive', 'Inactive'),
    ]

    # Basic Info
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='listings'
    )
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)

    # Owner (jo user ne add kiya)
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='listings',
        null=True,
        blank=True
    )

    # Contact Info
    phone = models.CharField(max_length=15, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    # Location
    address = models.CharField(max_length=300, blank=True)
    area = models.CharField(max_length=100, blank=True, help_text="e.g. Civil Lines, Gandhi Chowk")
    city = models.CharField(max_length=100, default='Guna')
    state = models.CharField(max_length=100, default='Madhya Pradesh')
    pincode = models.CharField(max_length=6, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Media
    cover_image = models.ImageField(upload_to='listings/covers/', blank=True, null=True)

    # Business Details
    business_hours = models.CharField(
        max_length=200,
        blank=True,
        help_text="e.g. Mon-Sat: 9am - 8pm, Sunday Closed"
    )
    established_year = models.PositiveIntegerField(null=True, blank=True)
    gst_number = models.CharField(max_length=20, blank=True)

    # Social Media
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    # Status & Flags
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_featured = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    # Stats
    views = models.PositiveIntegerField(default=0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Listing.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_whatsapp_link(self):
        number = self.whatsapp or self.phone
        return f"https://wa.me/91{number}" if number else ""

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    """Multiple images per listing"""
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='listings/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.listing.title} - Image {self.order}"


class ListingReview(models.Model):
    """User reviews for listings"""
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'user')  # ek user ek hi review de sakta

    def __str__(self):
        return f"{self.user} - {self.listing.title} ({self.rating}★)"
    
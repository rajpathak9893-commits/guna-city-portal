# businesses/admin.py

from django.contrib import admin
from .models import Category, Listing, ListingImage, ListingReview


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 2
    fields = ['image', 'caption', 'order']


class ListingReviewInline(admin.TabularInline):
    model = ListingReview
    extra = 0
    readonly_fields = ['user', 'rating', 'comment', 'created_at']
    can_delete = False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'icon']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'category',
        'owner',
        'city',
        'area',
        'phone',
        'status',
        'is_featured',
        'is_verified',
        'views',
        'created_at',
    ]

    list_filter = [
        'status',
        'is_featured',
        'is_verified',
        'category',
        'city',
    ]

    search_fields = [
        'title',
        'phone',
        'whatsapp',
        'email',
        'address',
        'area',
        'owner__username',
    ]

    prepopulated_fields = {'slug': ('title',)}

    readonly_fields = ['views', 'created_at', 'updated_at']

    list_editable = ['status', 'is_featured', 'is_verified']

    list_per_page = 25

    inlines = [ListingImageInline, ListingReviewInline]

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'owner', 'status')
        }),
        ('Description', {
            'fields': ('short_description', 'description')
        }),
        ('Contact Info', {
            'fields': ('phone', 'whatsapp', 'email', 'website')
        }),
        ('Location', {
            'fields': ('address', 'area', 'city', 'state', 'pincode', 'latitude', 'longitude')
        }),
        ('Business Details', {
            'fields': ('business_hours', 'established_year', 'gst_number')
        }),
        ('Social Media', {
            'fields': ('facebook', 'instagram'),
            'classes': ('collapse',)
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
        ('Flags & Stats', {
            'fields': ('is_featured', 'is_verified', 'views', 'created_at', 'updated_at')
        }),
    )


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ['listing', 'caption', 'order']
    list_filter = ['listing__category']
    search_fields = ['listing__title', 'caption']


@admin.register(ListingReview)
class ListingReviewAdmin(admin.ModelAdmin):
    list_display = ['listing', 'user', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['listing__title', 'user__username', 'comment']
    readonly_fields = ['created_at']
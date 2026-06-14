from django.contrib import admin
from .models import Job


def approve_jobs(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_jobs.short_description = "✅ Selected jobs approve karo"


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display   = ['title', 'company', 'job_type', 'location', 'is_approved', 'created_at']
    list_editable  = ['is_approved']
    list_filter    = ['is_approved', 'job_type']
    search_fields  = ['title', 'company']
    ordering       = ['-created_at']
    actions        = [approve_jobs]
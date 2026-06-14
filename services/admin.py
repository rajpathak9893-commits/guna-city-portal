from django.contrib import admin
from .models import Service


# Custom action — ek click mein multiple approve
def approve_services(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_services.short_description = "✅ Selected services approve karo"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'location', 'phone', 'is_approved', 'created_at']
    list_editable = ['is_approved']   # ← Seedha list se toggle kar sakte ho
    list_filter   = ['category', 'is_approved', 'availability']
    search_fields = ['name', 'location', 'category']
    ordering      = ['-created_at']
    actions       = [approve_services]  # ← Bulk approve ka button
from django.contrib import admin
from .models import School, College, Coaching,Education


admin.site.register(School)
admin.site.register(College)
admin.site.register(Coaching)
# from django.contrib import admin
# from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'location',
        'featured',
        'admission_open',
        'created_at'
    )

    list_filter = (
        'category',
        'featured',
        'admission_open'
    )

    search_fields = (
        'name',
        'location'
    )
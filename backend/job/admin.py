from django.contrib import admin
from job.models import Job

# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("company_name", "job_description", "job_type", "skills","reference_name")
from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class JobAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "first_name", "last_name", "email","username","verified")
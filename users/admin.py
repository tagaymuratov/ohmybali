from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  ordering = ('email',)
  list_display = ("email", "first_name", "last_name", "phone", "is_staff")
from django.contrib import admin
from account.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'education_level']
    raw_id_fields = ['user']
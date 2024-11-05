from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import Student, Program, Student_Profile, CohortGroup

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'status', 'cohort', 'rating', 'date_joined', 'profile_image_tag']  # Display profile_image as image

    # Create a method to render the profile image in the admin
    def profile_image_tag(self, obj):
        if obj.profile_picture:
            # return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;">', obj.profile_picture)
            return mark_safe(f'<img src="{obj.profile_picture.url}" width="50" height="50" />')
        return 'No Image'
    
    # Set the short description for this field in the admin
    profile_image_tag.short_description = 'Profile Image'

@admin.register(Student_Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student', 'date_of_birth', 'rating', 'date_join', 'address']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CohortGroup)
class CohortAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_join']

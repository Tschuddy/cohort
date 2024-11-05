# from django import forms
# from .models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['profile_image', 'full_name', 'cohort', 'program', 'status', 'date_joined', 'rating']
#         widgets = {
#             'date_joined': forms.DateInput(attrs={'type': 'date'}),
#             'rating': forms.NumberInput(attrs={'min': '1', 'max': '5'}),
#         }


from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'cohort', 'program', 'status', 'date_joined', 'rating']
       
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Student
from .models import Student, Program
from django.core.paginator import Paginator  # Import Paginator

class HompageView(View):
    def get(self, request):
        return render(request, 'index.html')


from django.shortcuts import render, get_object_or_404


def profile_view(request, user_id):
    # Retrieve the student object or return a 404 if not found
    user = get_object_or_404(Student, id=user_id)
    
    # Get students in the same cohort as the related students
    related_students = Student.objects.filter(cohort=user.cohort).exclude(id=user.id)[:3]

    # Pass the user and related students to the template
    return render(request, 'profile.html', {'user': user, 'related_students': related_students})

def add_user(request):

    if request.method == 'POST':
        profile_picture = request.POST['profile_picture'] 
        full_name = request.POST['full_name']
        cohort = request.POST['cohort']
        date_joined = request.POST['date_joined']
        program_id = request.POST['program']
        rating = request.POST['rating']
        status = request.POST['status']

        # Create and save the Student instance
        new_student = Student(
            profile_picture=profile_picture,
            full_name=full_name,
            cohort=cohort,
            date_joined=date_joined,
            program=program_id,
            rating=rating,
            status=status
        )
        new_student.save() 
    
        # Save to the databas
        return redirect('home')  # Redirect after successful addition

from django.views.generic import View
from .models import Student

class HompageView(View):
    def get(self, request):
        users = Student.objects.all()  # Fetch all users
        return render(request, 'index.html', {'users': users})
    

    from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from .models import Student

class HompageView(View):
    def get(self, request):
        users = Student.objects.all()  # Fetch all users
        paginator = Paginator(users, 2)  # Show 10 users per page
        
        # Get the current page number from the request
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'index.html', {'page_obj': page_obj})

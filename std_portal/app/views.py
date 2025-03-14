from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('instructor_dashboard')
            return redirect('dashboard')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    assignments = Assignment.objects.all()
    submissions = Submission.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {'assignments': assignments, 'submissions': submissions})

@login_required
def instructor_dashboard(request):
    assignments = Assignment.objects.filter(instructor=request.user)
    submissions = Submission.objects.filter(assignment__in=assignments)

    return render(request, 'instructor_dashboard.html', {'assignments': assignments,'submissions': submissions})

@login_required
def submit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == 'POST' and request.FILES['file']:
        Submission.objects.create(student=request.user, assignment=assignment, file=request.FILES['file'])
        return redirect('dashboard')
    return render(request, 'submit.html', {'assignment': assignment})


def add_assignment(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        if title and due_date:
            Assignment.objects.create(
                title=title, 
                description=description, 
                due_date=due_date, 
                instructor=request.user
            )
            return redirect("instructor_dashboard")

    return render(request, "add_assignment.html")

@login_required
def edit_assignment(request, assignment_id):
    assignment = Assignment.objects.get( id=assignment_id, instructor=request.user)

    if request.method == "POST":
        assignment.title = request.POST.get("title")
        assignment.description = request.POST.get("description")
        assignment.due_date = request.POST.get("due_date")
        assignment.save()
        return redirect("instructor_dashboard")

    return render(request, "edit_assignment.html", {"assignment": assignment})

@login_required
def delete_assignment(request, assignment_id):
    assignment = Assignment.objects.get( id=assignment_id, instructor=request.user)
    assignment.delete()
    return redirect("instructor_dashboard")

@login_required
def grade_submission(request, submission_id):
    submission = Submission.objects.get( id=submission_id)

    if request.method == "POST":
        submission.grade = request.POST.get("grade")
        submission.feedback = request.POST.get("feedback")
        submission.save()
        return redirect("instructor_dashboard")

    return render(request, "grade_submission.html", {"submission": submission})



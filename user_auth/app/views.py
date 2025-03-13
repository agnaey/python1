from django.shortcuts import render, redirect
from .models import Employee, Designation

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        experience = request.POST['experience']
        designation_id = request.POST['designation']
        profile_photo = request.FILES.get('profile_photo')

        if password != confirm_password:
            return render(request, 'register.html', {'error': "Passwords don't match"})

        try:
            designation = Designation.objects.get(id=designation_id)
        except Designation.DoesNotExist:
            return render(request, 'register.html', {'error': "Invalid designation"})

        user = Employee(
            username=username,
            email=email,
            experience=experience,
            designation=designation,
            profile_photo=profile_photo
        )
        user.set_password(password)  
        user.save()

        return redirect('login')

    designations = Designation.objects.all()
    return render(request, 'register.html', {'designations': designations})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Employee.objects.get(email=email)
            if user.check_password(password):
                request.session['user_id'] = user.id 
                return redirect('home')
        except Employee.DoesNotExist:
            pass

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = Employee.objects.get(id=user_id)
    return render(request, 'home.html', {'user': user})

def logout_view(request):
    request.session.flush() 
    return redirect('login')


Designation.objects.create(name="Software Engineer")
Designation.objects.create(name="Project Manager")
Designation.objects.create(name="HR Manager")
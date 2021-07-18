from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.


def login_reg(request):
    return render(request, 'login_reg.html')


def create_user(request):
    errors = User.objects.user_validator(request.POST)
    user_list = User.objects.filter(email = request.POST['email'])
    if user_list:
        messages.error(request, "Email already exists")
        return redirect('/')

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    print(request.POST['password'])
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    print(hashed_pw)

    user1 = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw,
    )
    request.session['log_user_id'] = user1.id
    return redirect('/dashboard')


def login_user(request):
    user_list = User.objects.filter(email = request.POST['email'])
    if user_list:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/')
    messages.error(request, "Email does not exist")
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
        



def dashboard(request):
    context = {
        'user': User.objects.get(id = request.session['log_user_id'])
    }
    return render(request, 'dashboard.html', context)
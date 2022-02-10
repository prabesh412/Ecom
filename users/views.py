from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST.get('email',False))
                return render(request, 'users/signup.html', {'error': 'user has already register'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('email',False), password=request.POST.get('password1'))
                return redirect('login')

        else:
            return render(request, 'users/signup.html', {'error': 'password must match'})  
    return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('email'),password=request.POST.get('password1'))
        if user:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('frontpage')
        else:        
            return render(request, 'users/login.html',{'error1': 'email or password incorrect'})
    return render(request, 'users/login.html')


def logout(request):
    django_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('frontpage')
    
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
from django.views.generic import View


class SignupView(View):

    def get(self, request):
        return render(request, 'signup.html', {'user_exist': False})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
        except:
            return render(request, 'signup.html', {'user_exist': True})
        auth_login(request, user=user)
        print(username, 'loged in')
        return redirect('home')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'check_pass': False})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                auth_login(request, user=user)
                print(username, 'loged in')
                return redirect('home')
            else:
                return render(request, 'login.html', {'check_pass': True})
        except:
            return render(request, 'login.html', {'check_pass': True})


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        auth_logout(request)
        return render(request, 'login.html', {'check_pass': False})
from django.shortcuts import render, redirect
from extra_project.models import *
from django.views import View
from extra_project.forms import *
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
import json

# Create your views here.


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        organizations = Institution.objects.all()
        quantity = [donation.quantity for donation in donations]
        org_a = Institution.objects.filter(type='a')
        org_b = Institution.objects.filter(type='b')
        org_c = Institution.objects.filter(type='c')
        if request.user.is_authenticated:
            log = 1
            user = request.user.first_name
        else:
            log = 0
            user = ''
        data = {
            'worki': sum(quantity),
            'organizacje': len(organizations),
            'org_a' : org_a,
            'org_b' : org_b,
            'org_c' : org_c,
            'logged': log,
            'user': user
        }
        return render(request, 'index.html', data)

    def post(self, request):
        if 'logout' in request.POST:
            logout(request)
            return redirect('/')
        if 'admin' in request.POST:
            logout(request)
            return redirect('/admin/')

class Login(View):
    def get(self, request, message=''):
        context = {
            'mess': message,
            'form': LoginForm
        }
        return render(request, 'login.html', context)
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            email = data.get('email')
            password = data.get('password')

            # uwierzytelnienie
            user = authenticate(
                username=email,
                password=password
            )
        if user:
            # logowanie
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register/')

class Register(View):
    def get(self, request):
        return render(request, 'register.html', {'form': Signup()})
    def post(self, request):
        if 'register' in request.POST:
            form = Signup(request.POST)
            if form.is_valid():
                data = form.cleaned_data

                User.objects.create_user(
                    username=data.get('email'),
                    password=data.get('password'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    email=data.get('email')
                )
                user = User.objects.get(username=data.get('email'))
                return redirect('/login/')

def home_4(request):
    return render(request, 'form-confirmation.html')

class Donate(View):
    def get(self, request):
        if request.user.is_authenticated:
            cat = Category.objects.all()
            institutions = Institution.objects.all()
            inst_cat = CategoriesInst.objects.all()

            return render(request, 'form.html', {'logged': 1,
                                                 'user': request.user.first_name,
                                                 'cat' : cat,
                                                 'institutions' : institutions,
                                                 'inst_cat' : inst_cat,
                                                })
        else:
            return redirect('/login')

    def post(self, request):
        if 'logout' in request.POST:
            logout(request)
            return redirect('/')
        if 'admin' in request.POST:
            logout(request)
            return redirect('/admin/')


class Profile(View):
    def get(self, request):
        donations = Donation.objects.filter(user_id=request.user.id)
        return render(request, 'profile.html', {'user': request.user, 'donations':donations})


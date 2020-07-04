from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from passlib.hash import pbkdf2_sha256
# Create your views here.
from .models import User 
from .form import RegisterForm, LoginForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class RegisterView(TemplateView):
    template_name = 'polls/login.html'

    def get(self,request):
        form = RegisterForm()
        login_form = LoginForm()
        context = {
            'form' :  form,
            'app_name' : "my_Link",
            "login_form" : login_form
        }
        return render(request, self.template_name,context)

    def post(self,request): 
        form =  RegisterForm(request.POST)
        login_form = LoginForm(request.POST)
        if request.method=='POST' and 'register' in request.POST:
            print("register")
            if form.is_valid():
                print("register")
                first = form.cleaned_data['firstname']
                last = form.cleaned_data['lastname']
                nickname = form.cleaned_data['nickname']
                password = form.cleaned_data['password']
                password_hashed = pbkdf2_sha256.encrypt(password,rounds=1200, salt_size=10)
                print(password_hashed)
                email = form.cleaned_data['email']
                terms = form.cleaned_data['aggrewithterm']
                user = User(nickname=nickname,firstname=first,lastname=last,password=password_hashed,email=email)
                user.save()
                return HttpResponseRedirect('')

        if request.method=='POST' and 'login' in request.POST:
            if login_form.is_valid():
                nickname = login_form.cleaned_data['nickname']
                ent_password = login_form.cleaned_data['password']
                try:
                    user = User.objects.get(nickname=nickname)
                except(KeyError, User.DoesNotExist):
                    context = {
                         'form' :  form,
                         'app_name' : "my_Link",
                         "login_form" : login_form,
                         "err_msg" : "The username you entered doesn't belong to an account."
                    }               
                    return render(request, self.template_name,context)

                user_pass = user.password
                if pbkdf2_sha256.verify(ent_password, user_pass):
                    return HttpResponseRedirect('')
                else:
                    context = {
                         'form' :  form,
                         'app_name' : "my_Link",
                         "login_form" : login_form,
                         "err_msg" : "Your password was incorrect."
                    }               
                    return render(request, self.template_name,context)
        
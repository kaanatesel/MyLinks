from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from passlib.hash import pbkdf2_sha256
from django.urls import reverse
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
            if form.is_valid():
                first = form.cleaned_data['firstname']
                last = form.cleaned_data['lastname']
                nickname = form.cleaned_data['nickname']
                password = form.cleaned_data['password']
                password_hashed = pbkdf2_sha256.encrypt(password,rounds=1200, salt_size=10)
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
                    response = HttpResponseRedirect(reverse('polls:userdetail', args=(user.id,)))
                    auth = "auth"
                    auth_hased = pbkdf2_sha256.encrypt(auth,rounds=1200, salt_size=10)
                    response.set_cookie("auth",auth_hased)
                    return response
                else:
                    context = {
                         'form' :  form,
                         'app_name' : "my_Link",
                         "login_form" : login_form,
                         "err_msg" : "Your password was incorrect."
                    }               
                    return render(request, self.template_name,context)

class UserDetailView(TemplateView): 
    template_name = 'polls/userdetail.html'

    def get(self,request,user_id):
        user = User.objects.get(id=user_id)

        auth = request.COOKIES.get('auth')
        context = {
            'app_name' : "my_Link",
            'usernickname' : user.nickname,
            'userfirstname' : user.firstname,
            'userlastname' : user.lastname,
            'auth' : auth
        }
        if auth == None:
            return HttpResponseRedirect('/polls/register')
        elif pbkdf2_sha256.verify("auth", auth):
            return render(request, self.template_name,context)
        else:
            return HttpResponseRedirect('polls/register')




from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
# Create your views here.
from .models import User 
from .form import RegisterForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class LoginView(TemplateView):
    template_name = 'polls/login.html'

    def get(self,request):
        print("get") 
        form = RegisterForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request): 
        print("post")
        form =  RegisterForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['firstname']
            last = form.cleaned_data['lastname']
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            terms = form.cleaned_data['aggrewithterm']
            print(first)
            print(last)
            user = User(nickname=nickname,firstname=first,lastname=last,password=password,email=email)
            user.save()
            print("git db bak")
            return HttpResponseRedirect('')
        
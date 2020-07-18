
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from passlib.hash import pbkdf2_sha256
from django.urls import reverse
# Create your views here.
from .models import User, Link
from .form import ChanageUserInforForm, UserDesForm, LinkForm

class UserDetailView(TemplateView): 
    template_name = 'polls/userdetail.html'

    def get(self,request,user_id):
        user = User.objects.get(id=user_id)
        userdes = user.description
        auth = request.COOKIES.get('auth')
        changeNameForm = ChanageUserInforForm()
        desForm = UserDesForm()
        linkForm = LinkForm()
        context = {
            'app_name' : "my_Link",
            'usernickname' : user.nickname,
            'userfirstname' : user.firstname,
            'userlastname' : user.lastname,
            'changeNameForm' : changeNameForm,
            'description' : userdes,
            'desform' : UserDesForm,
            'linkForm' : linkForm
        }
        if auth == None:
            return HttpResponseRedirect('/polls/register')
        elif pbkdf2_sha256.verify("auth", auth):
            return render(request, self.template_name,context)
        else:
            return HttpResponseRedirect('polls/register')

    def post(self,request,user_id):
        changeNameForm = ChanageUserInforForm(request.POST)
        desForm = UserDesForm(request.POST) 
        linkForm = LinkForm(request.POST)
        if request.POST and 'change_name' in request.POST:
            if changeNameForm.is_valid():
                newname = changeNameForm.cleaned_data['firstname']
                newlastname = changeNameForm.cleaned_data['lastname']
                try:
                   user = User.objects.get(id=user_id)               
                   user.firstname = newname
                   user.lastname = newlastname
                   user.save()
                   return HttpResponseRedirect(self.request.path_info)
                except (KeyError, User.DoesNotExist):
                   context = {
                       'app_name' : "my_Link",
                       'usernickname' : user.nickname,
                       'userfirstname' : user.firstname,
                       'userlastname' : user.lastname,
                       'changeNameForm' : changeNameForm,
                       'desform' : UserDesForm,
                       'err_msg' : "Some thing went wrong try again.",
                        'linkForm' : linkForm
                   }
                   return render(request, self.template_name,context)

        if request.POST and 'change_des' in request.POST:
            if desForm.is_valid():
                newdes = desForm.cleaned_data['Description']
                try:
                    user = User.objects.get(id=user_id)               
                    user.description = newdes
                    user.save()
                    return HttpResponseRedirect(self.request.path_info)
                except (KeyError, User.DoesNotExist):
                   context = {
                       'app_name' : "my_Link",
                       'usernickname' : user.nickname,
                       'userfirstname' : user.firstname,
                       'userlastname' : user.lastname,
                       'changeNameForm' : changeNameForm,
                       'desform' : UserDesForm,
                       'err_msg' : "Some thing went wrong try again.",
                       'linkForm' : linkForm
                   }
                   return render(request, self.template_name,context)  

        if request.POST and 'add_link' in request.POST:
            if linkForm.is_valid():
                print("link is valid")
                linkname = linkForm.cleaned_data['linkname']
                linkurl = linkForm.cleaned_data['url']
                linkcolor = linkForm.cleaned_data['color']
                try:
                   user = User.objects.get(id=user_id)
                except (KeyError, User.DoesNotExist):
                   context = {
                       'app_name' : "my_Link",
                       'usernickname' : user.nickname,
                       'userfirstname' : user.firstname,
                       'userlastname' : user.lastname,
                       'changeNameForm' : changeNameForm,
                       'desform' : UserDesForm,
                       'err_msg' : "Some thing went wrong try again.",
                        'linkForm' : linkForm
                   }
                   return render(request, self.template_name,context)
                newLink = Link(name=linkname,url=linkurl,color_code=linkcolor,user_id=user)
                newLink.save()
                return HttpResponseRedirect(self.request.path_info)


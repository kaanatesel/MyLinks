from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def login(request):
    template = loader.get_template('polls/login.html')
    context = {
        'app_name' : 'my-Links'
    }
    return HttpResponse(template.render(context,request))

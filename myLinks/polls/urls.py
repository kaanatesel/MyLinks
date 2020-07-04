from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view() , name='register'),
    path('<int:user_id>/userdetail/', views.UserDetailView.as_view() , name='userdetail'),
]
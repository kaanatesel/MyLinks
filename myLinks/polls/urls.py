from django.urls import path

from . import views
from . import UserDetailView

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view() , name='register'),
    path('<int:user_id>/userdetail/', UserDetailView.UserDetailView.as_view() , name='userdetail'),
]
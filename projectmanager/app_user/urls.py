from django.urls import path
from . import views

app_name = 'app_user'
urlpatterns = [
    path('', views.UserView.as_view(), name='users')
]
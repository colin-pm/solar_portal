from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'portal'
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('weather', views.weather, name='weather'),
    path('watering', views.watering, name='watering'),
    path('login', auth_views.LoginView.as_view(template_name="../templates/login.html"), name='login'),
    path('logout', views.logout_view, name="logout")
]

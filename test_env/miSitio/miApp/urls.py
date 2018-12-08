from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('oauth', views.logged, name='logged'),
]
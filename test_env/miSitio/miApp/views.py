from django.shortcuts import render

#DJANGO-social
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'miApp/home.html', {})

#LOG con red social
@login_required
def logged(request):
    return render(request, 'miapp/logged.html')
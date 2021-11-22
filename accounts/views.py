from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import RegistraForm
from django.contrib.auth import authenticate, login

def register(request):
    template_name = 'registration/register.html'
    if request.method == 'POST':
        form = RegistraForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect(settings.LOGIN_URL)
    else:
        form = RegistraForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

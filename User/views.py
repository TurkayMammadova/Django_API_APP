
from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    context= {}
    context['form'] = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                print('User is here!!!')
                return redirect('profile/')

    return render(request, 'login.html', context)


@login_required
def profile_view(request):
	return render(request,'profile.html')
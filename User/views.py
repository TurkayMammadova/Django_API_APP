from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.views.generic.base import ContextMixin
from Currency.models import Menu
from .forms import UserRegistrationForm , LoginForm
from django.contrib.auth.decorators import login_required


# def nav_bar(request):
#     print('MAhir')
#     dates = []
#     nav_bar = Menu.objects.all()
#     print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     print(nav_bar)
#     print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     for nav in nav_bar:
#         data = {
#             'url': nav.url_address,
#             'name': nav.name
#         }
#         dates.append(data)
#     context = {
#         'dates': dates
#     }

#     return render(request, 'base.html',context)

# class NavView(ContextMixin):
#     def get_context_data(self, *args,**kwargs):
#             context = super().get_context_data(*args, **kwargs)
#             context["nav_links"] = Menu.objects.all()
#             return context



# @login_required(redirect_field_name='home')
def home(request):
    return render(request, 'home.html')


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')

    context = {'form': form}
    return render(request, 'auth/register.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
           
                return redirect('home')

    context = {'form': form}    
    return render(request, 'auth/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login') 



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import UserRegisterForm, ProfileForm,UserLoginForm
from .models import Profile
from django.contrib.auth.decorators import login_required  # Add this import


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Automatically set user_type to Customer (0)
            Profile.objects.create(user=user, user_type=Profile.CUSTOMER)

            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
    else:
        user_form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})





def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if Profile.objects.get(user=user).user_type == 'admin':
                return redirect('company_page')
            else:
                return redirect('product_page')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def company_page(request):
    return render(request, 'accounts/company_page.html')

@login_required
def product_page(request):
    return render(request, 'accounts/product_page.html')


def home(request):
    return render(request, 'accounts/home.html')
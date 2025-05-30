from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
@login_required
def logIn(request):
    return redirect('menu')
def singIn(request):
    
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        user_creation_form=CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user=authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('menu')
    return render(request, 'users/singin.html', data)
def logOut(request):
    logout(request)
    return redirect('menu')
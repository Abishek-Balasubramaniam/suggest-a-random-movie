from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
def account_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('random_movies:random_movie')
    else:
        form=UserCreationForm()
    return render(request,'accounts/accounts.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return  redirect(request.POST.get('next'))
            else:
                return redirect('random_movies:random_movie')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('random_movies:random_movie')
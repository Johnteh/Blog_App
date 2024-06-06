from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account as succesfully created. Please log in')
            return redirect('login')
    else:
        form = UserRegisterForm(request.POST)


    
    return render(request, 'users/register.html', {'form': form})
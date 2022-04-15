from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register new users"""
    if request.method != 'POST':
        # Display empty registration form
        form = UserCreationForm()
    else:
        # Process completed forms
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Let users log in automatically and redirect to the home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Displays an empty form or indicates that the form is invalid
    context = {'form': form}
    return render(request, 'registration/register.html', context)

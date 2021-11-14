from django.shortcuts import render, redirect
from management.forms import ProfileForm


# Create your views here.
def index(request):
    pass


def UserProfile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error")
        return render(request, '/templates/index.html', {'form': form})

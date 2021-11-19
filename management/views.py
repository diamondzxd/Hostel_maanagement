from django.shortcuts import render, redirect
from management.forms import ProfileForm, PaymentForm, RoomForm


# Create your views here.
def index(request):
    return render(request, "management/index.html")


def users(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, "management/user.html", {'form': form})

def rooms(request):
    form = RoomForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, "management/room.html", {'form': form})
from django.http import HttpResponse
from django.shortcuts import render, redirect
from management.models import Profile
from management.forms import ProfileForm, PaymentForm, RoomForm


# Create your views here.
def index(request):
    return render(request, "management/index.html")


def AddUser(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, "management/user.html", {'form': form})


def DisplayStudents(request):
    students = Profile.objects.all()
    # SELECT * FROM profile
    return render(request, 'management/displayStudents.html', {'students': students})


def DeleteStudent(request, id):
    student = Profile.objects.get(id=id)
    student.delete()
    return redirect('/DisplayStudents/')


def AddRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, "management/room.html", {'form': form})
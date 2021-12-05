from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from management.models import Profile, Room
from management.forms import ProfileForm, PaymentForm, RoomForm


# Create your views here.
def index(request):
    return render(request, "management/index.html")


def RegisterUser(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, "management/user.html", {'form': form})
    # return render(request, "management/user.html", {'form': form})


def UpdateUser(request, id):
    method = request.method
    if method == 'GET':
        student = Profile.objects.filter(id=id).values().first()
        data = {'form': ProfileForm(student)}
        return render(request, 'management/user.html', data)
    elif method == 'POST':
        student = Profile.objects.get(id=id)
        form = ProfileForm(request.POST, instance=student)
        form.save()
        return redirect('/DisplayStudents/')


def DisplayStudents(request):
    students = Profile.objects.all()
    room = Room.objects.all()
    details = {'students': students, 'room': room}
    # SELECT * FROM profile
    return render(request, 'management/displayStudents.html', details)


def DeleteStudent(request, id):
    student = Profile.objects.get(id=id)
    student.delete()
    return redirect('/DisplayStudents/')


def AddRoom(request):
    if request.method == 'GET':
        form = RoomForm()
        return render(request, "management/room.html", {'form': form})
    else:
        form = RoomForm(request.POST)
        # if form.is_valid():
        form.save()
        return HttpResponse('Form Saved Succesfully!')

    # return render(request, "management/room.html", {'form': form})


# def UpdateRoom(request, category):
#     method = request.method
#     if method == 'GET':
#         room = Room.objects.filter(category=category).values()
#         data = {'form': RoomForm(room)}
#         return render(request, 'management/room.html', data)
#     elif method == 'POST':
#         room = Room.objects.get(category=category)
#         form = RoomForm(request.POST, instance=room)
#         form.save()
#         return redirect('/DisplayRoom/')


def DisplayRoom(request):
    rooms = Room.objects.all()
    details = {'rooms': rooms}
    print(details)
    return render(request, 'management/displayRoom.html', details)
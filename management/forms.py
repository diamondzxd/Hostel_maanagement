from django import forms
from django.contrib.auth.forms import UserCreationForm

from management.models import Profile, Room, Payment, Subscription


#
# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'birth_date', 'password1', 'password2', )
#


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail ID', 'class': 'form-control'}))
    enrollment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enrollment', 'class': 'form-control'}))
    course = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Course', 'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'phone no.', 'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateTimeInput(attrs={'placeholder': 'Date of birth', 'class': 'form-control','type': 'date'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))


#
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Login
#         fields = ["email", "password"]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        # student = forms.Select(widget=forms.Select(attrs={'placeholder': 'Select', 'class': 'form-control'}))


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'
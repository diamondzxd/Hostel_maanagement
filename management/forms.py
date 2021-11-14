from django import forms
from management.models import Profile,Room,Payment,User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('enrollment', 'course', 'phone', 'dob' ,'address')

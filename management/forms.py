from django import forms
from management.models import Profile,Room,Payment,User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    #first_name = forms.CharField(widget=forms.TextInput )
    #last_name = forms.CharField(widget=forms.TextInput)
    #enrollment = forms.CharField(widget=forms.TextInput)
    #email = forms.EmailField(widget=forms.EmailField)
    #course = forms.CharField(widget=forms.TextInput)
    #phone = forms.CharField(widget=forms.TextInput)
    #dob = forms.DateField(widget=forms.DateField)
    #address = forms.CharField(widget=forms.TextInput)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'






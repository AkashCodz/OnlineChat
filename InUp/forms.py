from django import forms
from .models import UserProfile

class UserRegistration(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields = ['username','gender','country','email','password','password2']


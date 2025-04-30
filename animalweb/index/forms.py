from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email'] 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['bio', 'profile_picture']    

from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

from django import forms
from .models import Selling

class SellingForm(forms.ModelForm):
    class Meta:
        model = Selling
        fields = ['name', 'address', 'mobile_number', 'animal_name', 'animal_image', 'animal_price', 'description']


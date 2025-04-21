from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import Record  # Ensure this import is correct

# Registration form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login form
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))

# Contact form
class ContactForm(forms.ModelForm):  
  class Meta:
        model = Record  # FIXED: 'models' → 'model'
        fields = ['first_name', 'last_name', 'email', 'phone_number']  


class UpdateForm(forms.ModelForm):
  class Meta:
        model = Record  
        fields = ['first_name', 'last_name', 'email', 'phone_number']
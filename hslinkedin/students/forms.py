from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from models import USA_COUNTIES

class UserRegisterForm(UserCreationForm):
    display_name = forms.CharField(max_length=150)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    county = forms.ChoiceField(choices=USA_COUNTIES)
    interests = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'display_name', 'birthday', 'county', 'interests', 'password1', 'password2']
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Studio
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    # last_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class StudioForm(ModelForm):
    class Meta:
        model = Studio
        fields = ['studio_name', 'studio_details', 'studio_type', 'past_clients', 'audio_samples', 'equipments', 'address', 'price_per_hour', 'studio_image']

    
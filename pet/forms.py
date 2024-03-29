from django import forms
from .models import Pet, Owner
from django.forms.widgets import DateInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'pet_image', 'birthdate', 'gender', 'spayed_or_neutered', 'species','breed','care_notes', 'food_notes')

#class CommentForm(forms.ModelForm):
#   class Meta:
#        model = Comment
#        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'pet_image', 'birthdate', 'gender', 'spayed_or_neutered', 'species','breed','care_notes', 'food_notes')
        # Reference - https://stackoverflow.com/questions/41224035/django-form-field-label-how-to-change-its-value-if-it-belongs-to-a-certain-fi
        labels = {'visited_date': "Visited Date"}
        # Reference https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
        widgets = {'visited_date': DateInput(attrs={'type': 'date', 'placeholder':'Select a date'})}

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Required')
    last_name = forms.CharField(max_length=20, help_text='Required')
    email = forms.EmailField(max_length=60, help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

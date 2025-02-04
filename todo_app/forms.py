from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class CustomAuthenticationForm(AuthenticationForm):
    pass
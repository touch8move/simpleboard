from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        widgets = {
            'username': forms.fields.TextInput(attrs={
                'placeholder': 'ID',
                'class': 'form-control input-lg',
            }),
            'email': forms.fields.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control input-lg',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'PW1',
                'class': 'form-control input-lg',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'PW2',
                'class': 'form-control input-lg',
            }),
        }

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
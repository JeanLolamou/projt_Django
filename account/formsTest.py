from django.forms import ModelForm
from django import forms
from admin_app.models import *
from django.contrib.auth.models import User


class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
        # fields = ['titre', 'photo', 'categorie', 'prix', 'description', 'date_ajout']
        # fields = '__all__'
        exclude = ['user']

        widgets = {
            'titre': forms.TextInput(
                attrs={'class': 'form-control txt',
                       'placeholder': "Titre de l'annonce"}
            ),
            'photo': forms.ClearableFileInput(
                attrs={'class': 'form-controlfile txt'}
            ),
            'categorie': forms.Select(

                attrs={'class': 'form-control txt'}
            ),
            'prix': forms.NumberInput(
                attrs={'class': 'form-control txt',
                       'placeholder': "Prix de l'article"}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control txta',
                       'placeholder': "Description de l'annonce"}
            ),
            # 'date_ajout': forms.DateTimeInput(
            #     attrs={'class': 'form-control',
            #            'placeholder': "Ajoute le :"}
            # ),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'tel': forms.NumberInput(
                attrs={'class': 'form-control txt',
                       'placeholder': "+221 77 123 45 67"}
            ),
            'photo': forms.ClearableFileInput(
                attrs={'class': 'form-controlfile txt'}
            ),
        }


class UserForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control txt',
               'placeholder': "Confirm Password"}
    ))
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        widgets={
            'username': forms.TextInput(
                attrs={'class': 'form-control txt',
                    'placeholder': "Username"}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control txt',
                    'placeholder': "example@example.com"}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control txt',
                    'placeholder': "Password"}
            ),
        }


class loginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control txt',
                       'placeholder': "Username"}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control txt',
                       'placeholder': "Password"}
            ),
        }
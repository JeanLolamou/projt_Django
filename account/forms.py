from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _

class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("Les deux mots de passes ne correspondent pas"),
    }
    password2 = forms.CharField(
        label=("Password"),
        strip=False, 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control ',
                   'placeholder': "Confirmer le mot de passe"}
        ),
        help_text="Ecrivez le même mot de passe",
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': _('username'),
        }
        help_texts = {
            'username': _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        }
        error_messages = {
            'username': {
                'max_length': _("This name is too long."),
            },
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control ',
                       'placeholder': "Ecrivez ici votre username"}
            ),
        }

class SigninForm (AuthenticationForm):
    pass

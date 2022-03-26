from django.contrib.auth import forms
from django import forms as d_forms

from .models import User

from allauth.account.forms import SignupForm
from allauth.account.forms import PasswordField

import string
from random import randint

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User

def createPassword():
    letters = list(string.ascii_lowercase)
    p = ''

    for i in range(4):
        p += letters[randint(0, len(letters)-1)]

    for i in range(4):
        p += str(randint(0, 9))

    return p

class UserSignupForm(SignupForm):
    # birth_date = d_forms.DateField(widget=d_forms.DateInput)
    birth_date = d_forms.DateField(widget=d_forms.DateInput(format='%d/%m/%Y', attrs={'data-mask':"00/00/0000"})) #widget=d_forms.widgets.DateInput(format='%Y-%m-%d')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"] = PasswordField(
            label=("Password"), autocomplete="new-password", required=False
        )

        self.fields.pop('email')

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(UserSignupForm, self).save(request)

        # Add your own processing here.

        user.birth_date = self.cleaned_data["birth_date"]

        if self.cleaned_data["password1"] in ["", " "]:
            user.password = createPassword()
            print("\n\n senha :", user.password)

        user.save()

        # You must return the original result.
        return user
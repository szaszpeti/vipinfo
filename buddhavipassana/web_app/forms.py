from django import forms
from .models import BuddhaRegister


class BuddhaRegisterForm(forms.ModelForm):
    class Meta():
        model = BuddhaRegister
        fields = '__all__'


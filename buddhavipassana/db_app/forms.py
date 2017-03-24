from django import forms
from django.contrib.auth.models import User
from db_app.models import Meditator

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site','profile_pic')

class MeditatorForm(forms.ModelForm):
    model = Meditator
    fields = '__all__'
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Profile

class UserForm(UserCreationForm):

    class Meta:
        model=User
        fields=('username','password1','password2','first_name','last_name','email')

BRANCHES=[
    ('IT','IT'),
    ('CSE','CSE'),
    ('ECE','ECE'),
    ('MEC','MECH'),
    ('ALL','ALL BRANCHES')
]
YEAR=[
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (0,'ALL YEARS')
]
SEC=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('T','ALL SECTIONS')
]


class ProfileForm(forms.Form):
    branch = forms.CharField(widget=forms.Select(choices=BRANCHES))
    year = forms.CharField(widget=forms.Select(choices=YEAR))
    sec = forms.CharField(widget=forms.Select(choices=SEC))
    class Meta:
        model=Profile
        fields=('branch','year','sec')

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password')

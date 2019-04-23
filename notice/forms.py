from django import forms
from . models import Notice
from django.utils import timezone
BRANCHES=[
    ('IT','IT'),
    ('CSE','CSE'),
    ('ECE','ECE'),
    ('MEC','MECH'),
    ('ALL','ALL BRANCHES')
]
YEAR=[
    (1,'IT'),
    (2,'CSE'),
    (3,'ECE'),
    (4,'MECH'),
    (0,'ALL YEARS')
]
SEC=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('T','ALL SECTIONS')
]
class PostNoticeForm(forms.ModelForm):
    '''branch=forms.CharField(widget=forms.Select(choices=BRANCHES))
    Year = forms.CharField(widget=forms.Select(choices=YEAR))
    sec = forms.CharField(widget=forms.Select(choices=SEC))
    date=forms.DateTimeField(initial=timezone.now())'''
    class Meta:
        model=Notice
        fields=('notice',)


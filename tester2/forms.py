from django import forms
from .models import employess
class enroll(forms.ModelForm):
     ename=forms.CharField(max_length=88)
     eno=forms.IntegerField()
     eid=forms.IntegerField()
     email=forms.CharField(max_length=99)
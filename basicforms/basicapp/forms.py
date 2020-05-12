from django import forms
from django.core import validators



class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    verify_email=forms.EmailField(label='confirm email:')


    def clean(self):
        clean_it= super().clean()
        m=clean_it['email']
        vm=clean_it['verify_email']
        if m!=vm:
            raise forms.ValidationError("should be same!!")

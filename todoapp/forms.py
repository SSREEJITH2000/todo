from django import forms

from . models import tasks
class ToDo_form(forms.ModelForm):
    class Meta:
        model=tasks
        fields=['names','priorities','dates']
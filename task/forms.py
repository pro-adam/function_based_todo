from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    title = forms.
    class Meta:
        model = Task
        fields = '__all__'
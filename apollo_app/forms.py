import datetime

from django import forms
from django.utils.safestring import mark_safe

from apollo_app.models import Task_Models, Task_Models_Post


class Task_Models_Form(forms.ModelForm):
    class Meta:
        model = Task_Models
        fields = '__all__'


class Task_Models_Form_post(forms.ModelForm):
    class Meta:
        model = Task_Models_Post
        fields = '__all__'

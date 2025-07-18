# todo/forms.py

from django import forms
from .models import Pendiente

class PendienteForm(forms.ModelForm):
    class Meta:
        model = Pendiente
        fields = ['userId', 'title', 'completed']
from django import forms
from .models import JobOrder

class JobOrderForm(forms.ModelForm):
    class Meta:
        model = JobOrder
        fields = '__all__'
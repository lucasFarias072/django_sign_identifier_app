

from django import forms
from .models import Sign


class SignModelForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ('birthday',)
        birthday = forms.CharField(max_length=100)

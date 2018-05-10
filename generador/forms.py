from django import forms
from .models import VariableLote1, VariableLote2


class VariableL1ModelForm(forms.ModelForm):
    class Meta:
        model = VariableLote1
        fields = ['valor']


class VariableL2ModelForm(forms.ModelForm):
    class Meta:
        model = VariableLote2
        fields = ['valor']

from django import forms
from .models import AkunSosmed


class AkunSosmedForm(forms.ModelForm):
    class Meta:
        model = AkunSosmed
        fields = [
            'nama_depan',
            'nama_belakang',
            'username',
        ]

from django import forms

from .models import Credito

class PostForm(forms.ModelForm):

    class Meta:
        model = Credito
        fields = ('monto_uf', 'plazo', 'fecha')